#!/usr/bin/env python3
"""Wayback Save Page Now driver for the references catalogue.

Reads `taxonomy/_references.md`, finds entries whose `Archive:` field is
empty or a placeholder, asks the Internet Archive's Save Page Now (SPN) v2
API to snapshot the corresponding `URL:`, waits for the snapshot to
finalise, and writes the resulting timestamped Wayback URL back into the
catalogue. The script is idempotent — already-archived entries are
skipped.

Usage
-----
    uv run python taxonomy/tools/snapshot.py            # snapshot anything pending
    uv run python taxonomy/tools/snapshot.py --dry-run  # show what would change
    uv run python taxonomy/tools/snapshot.py --handle DCB0129
                                              # snapshot one entry by handle (forces a re-fetch)
    uv run python taxonomy/tools/snapshot.py --refresh
                                              # re-snapshot all entries (rotates Archive URLs)

API
---
Save Page Now v2 (https://archive.org/help/wayback_api.php) requires no
key for read but anonymous capture requests are throttled. For unattended
runs you can set an Internet Archive S3-style key pair via env vars:

    IA_ACCESS_KEY=your-key
    IA_SECRET_KEY=your-secret

The script attempts authenticated capture if both env vars are present;
otherwise it falls back to an anonymous capture via the same endpoint.
Anonymous capture is fine for the v3.9 catalogue size (~38 URLs).

Rate limits
-----------
Wayback throttles aggressively. Default behaviour:
- 6-second pause between submissions
- Max 30 in-flight jobs at once (we pace one at a time)
- Up to 4 retries with exponential backoff per URL

If a URL refuses to snapshot (Wayback robots-blocked, JS-rendered, auth-
walled, etc.) the catalogue entry receives `Archive-Status: unavailable`
plus a reason; the audit treats this as a known limitation rather than a
blocking error.

Implementation notes
--------------------
This file deliberately uses only `urllib`-flavoured stdlib HTTP — no
extra runtime dependencies — so it works under uv-managed envs without
extra installs. Auth is via the IA's S3-style header pair.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field

# Add taxonomy/ to sys.path so the script can import parse.py directly.
HERE = os.path.dirname(os.path.abspath(__file__))
TAXONOMY_DIR = os.path.dirname(HERE)
if TAXONOMY_DIR not in sys.path:
    sys.path.insert(0, TAXONOMY_DIR)

import parse  # noqa: E402

REFERENCES_PATH = os.path.join(TAXONOMY_DIR, "_references.md")

SPN_BASE = "https://web.archive.org/save"
SPN_USER_AGENT = "avt-taxonomy-snapshot/1.0 (+https://github.com/danjscho/avt-metrics-taxonomy)"
PLACEHOLDER_PATTERNS = (
    "_(Phase 1",  # the v3.9 placeholder string
    "(pending)",
    "(unavailable)",
    "(skip)",
)


@dataclass
class SnapshotResult:
    handle: str
    url: str
    archive: str = ""
    status: str = "ok"  # ok | unavailable | error
    reason: str = ""


def _is_placeholder(archive_value: str) -> bool:
    if not archive_value.strip():
        return True
    for pat in PLACEHOLDER_PATTERNS:
        if pat in archive_value:
            return True
    if not archive_value.startswith("http"):
        return True
    return False


def _build_request(url: str) -> urllib.request.Request:
    """Build a Save Page Now v2 capture request.

    Posts to /save with form-encoded body containing the URL and capture
    options. Authenticates with IA S3 keys if available.
    """
    data = urllib.parse.urlencode(
        {
            "url": url,
            "capture_outlinks": "0",
            "capture_screenshot": "0",
            "skip_first_archive": "0",
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        SPN_BASE,
        data=data,
        method="POST",
    )
    req.add_header("User-Agent", SPN_USER_AGENT)
    req.add_header("Accept", "application/json")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    access = os.environ.get("IA_ACCESS_KEY")
    secret = os.environ.get("IA_SECRET_KEY")
    if access and secret:
        req.add_header("Authorization", f"LOW {access}:{secret}")
    return req


def _poll_job(job_id: str, timeout_s: int = 120) -> tuple[str, str]:
    """Poll the SPN status endpoint until the job is `success` or `error`.

    Returns (status, archive_url_or_reason). Status is one of:
    - `success` → archive_url_or_reason is the timestamped Wayback URL
    - `error` → archive_url_or_reason is the SPN error message
    - `timeout` → archive_url_or_reason explains
    """
    status_url = f"https://web.archive.org/save/status/{job_id}"
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        time.sleep(3)
        try:
            with urllib.request.urlopen(status_url, timeout=15) as resp:
                payload = json.load(resp)
        except (urllib.error.URLError, json.JSONDecodeError) as e:
            return "error", f"poll-failed: {e}"
        st = payload.get("status")
        if st == "success":
            ts = payload.get("timestamp")
            original = payload.get("original_url") or payload.get("url")
            if ts and original:
                return "success", f"https://web.archive.org/web/{ts}/{original}"
            return "error", "success without timestamp"
        if st == "error":
            return "error", payload.get("message") or payload.get("status_ext") or "spn-error"
        # else still 'pending' — keep polling
    return "timeout", f"job {job_id} did not finish in {timeout_s}s"


def snapshot_one(url: str, throttle_s: float = 6.0, retries: int = 3) -> SnapshotResult:
    """Submit one URL for snapshotting and return the resolved Wayback URL."""
    last_err = ""
    for attempt in range(retries + 1):
        if attempt:
            backoff = throttle_s * (2 ** (attempt - 1))
            print(f"    retry {attempt}/{retries} in {backoff:.0f}s ({last_err})")
            time.sleep(backoff)
        else:
            time.sleep(throttle_s)
        try:
            req = _build_request(url)
            with urllib.request.urlopen(req, timeout=30) as resp:
                payload = json.load(resp)
        except urllib.error.HTTPError as e:
            last_err = f"http {e.code}"
            continue
        except (urllib.error.URLError, json.JSONDecodeError, TimeoutError) as e:
            last_err = str(e)
            continue

        job_id = payload.get("job_id")
        if not job_id:
            # Some SPN errors come back with a `message` immediately
            return SnapshotResult(
                handle="",
                url=url,
                status="unavailable",
                reason=payload.get("message") or "no-job-id",
            )
        status, result = _poll_job(job_id)
        if status == "success":
            return SnapshotResult(handle="", url=url, archive=result, status="ok")
        last_err = result
        if status == "error" and "robot" in result.lower():
            # robots-disallowed snapshots are not retryable
            return SnapshotResult(handle="", url=url, status="unavailable", reason=result)
    return SnapshotResult(handle="", url=url, status="error", reason=last_err)


def parse_existing_catalogue() -> dict[str, parse.Reference]:
    """Reuse the parser from parse.py to read the catalogue."""
    return parse.parse_references()


def write_catalogue_with_archive(
    handle: str,
    archive: str,
    retrieved: str | None = None,
    status: str | None = None,
) -> None:
    """Patch the catalogue file in-place: set the Archive: line for one
    entry. Optionally update Retrieved:. If status='unavailable', the
    Archive: line records that plus reason and adds an Archive-Status:
    line as a sibling field.

    Implementation: line-by-line read/replace, scoped to the entry whose
    `### handle` heading we just passed.
    """
    path = REFERENCES_PATH
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    out: list[str] = []
    in_target = False
    for line in lines:
        m = re.match(r"^###\s+([A-Za-z0-9][A-Za-z0-9_-]*)\s*$", line)
        if m:
            in_target = m.group(1) == handle
            out.append(line)
            continue
        if in_target:
            if re.match(r"^-\s+\*\*Archive:\*\*", line):
                out.append(f"- **Archive:** {archive}")
                continue
            if re.match(r"^-\s+\*\*Retrieved:\*\*", line) and retrieved:
                out.append(f"- **Retrieved:** {retrieved}")
                continue
        out.append(line)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="report only; don't capture")
    ap.add_argument("--handle", help="snapshot one entry by handle (forces re-fetch)")
    ap.add_argument("--refresh", action="store_true", help="re-snapshot all entries")
    ap.add_argument("--throttle", type=float, default=6.0, help="seconds between submissions")
    args = ap.parse_args()

    catalogue = parse_existing_catalogue()
    if not catalogue:
        print("No catalogue entries; nothing to do.")
        return 0

    today = time.strftime("%Y-%m-%d")
    pending: list[parse.Reference] = []
    for handle, ref in catalogue.items():
        if args.handle and handle != args.handle:
            continue
        if args.refresh or _is_placeholder(ref.archive):
            if not ref.url:
                print(f"  [{handle}] no URL — skipping")
                continue
            pending.append(ref)

    if not pending:
        print("All catalogue entries already archived. Use --refresh to rotate.")
        return 0

    print(f"Snapshotting {len(pending)} entries (throttle={args.throttle}s)...")
    if args.dry_run:
        for ref in pending:
            print(f"  would snapshot [{ref.handle}] -> {ref.url}")
        return 0

    failures: list[SnapshotResult] = []
    for ref in pending:
        print(f"  [{ref.handle}] {ref.url}")
        result = snapshot_one(ref.url, throttle_s=args.throttle)
        result.handle = ref.handle
        if result.status == "ok":
            print(f"    archived: {result.archive}")
            write_catalogue_with_archive(result.handle, result.archive, retrieved=today)
        elif result.status == "unavailable":
            print(f"    UNAVAILABLE: {result.reason}")
            write_catalogue_with_archive(
                result.handle,
                f"_(unavailable: {result.reason})_",
            )
            failures.append(result)
        else:
            print(f"    ERROR: {result.reason}")
            failures.append(result)

    if failures:
        print(f"\n{len(failures)} entries did not archive cleanly.")
        for f in failures:
            print(f"  [{f.handle}] {f.status}: {f.reason}")
        return 1
    print("\nAll snapshots applied to _references.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
