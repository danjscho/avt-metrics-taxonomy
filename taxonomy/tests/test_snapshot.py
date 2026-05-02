"""Unit tests for taxonomy/tools/snapshot.py.

Pure-logic tests for the placeholder detector; one mocked-HTTP smoke test
for snapshot_one (the real Wayback Save-Page-Now API isn't testable in
CI, so we mock urllib.request.urlopen and assert the call sequence +
result handling).
"""
from __future__ import annotations

import io
import json
import pathlib
import sys
from unittest.mock import patch

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from tools import snapshot  # noqa: E402


# ---------------------------------------------------------------------------
# _is_placeholder
# ---------------------------------------------------------------------------


class TestIsPlaceholder:
    def test_empty_is_placeholder(self):
        assert snapshot._is_placeholder("") is True

    def test_whitespace_is_placeholder(self):
        assert snapshot._is_placeholder("   \n\t") is True

    def test_phase_1_marker_is_placeholder(self):
        assert (
            snapshot._is_placeholder("_(Phase 1 — pending snapshot.py)_") is True
        )

    def test_real_archive_url_is_not_placeholder(self):
        assert (
            snapshot._is_placeholder(
                "https://web.archive.org/web/20260415120000/example.com/dcb0129"
            )
            is False
        )

    def test_non_http_value_is_placeholder(self):
        # The function treats any non-http string as a placeholder, so
        # malformed values like "TBD" or "(pending)" are caught.
        assert snapshot._is_placeholder("TBD") is True
        assert snapshot._is_placeholder("(pending)") is True


# ---------------------------------------------------------------------------
# snapshot_one — mocked HTTP smoke tests
# ---------------------------------------------------------------------------


class _FakeResponse:
    """Minimal context-manager wrapper around a json payload, mimicking the
    interface urllib.request.urlopen returns (an http.client.HTTPResponse-
    like object whose `read()` returns bytes that json.load can consume)."""

    def __init__(self, payload: dict):
        self._payload = json.dumps(payload).encode("utf-8")

    def __enter__(self):
        return io.BytesIO(self._payload)

    def __exit__(self, *args):
        return False


class TestSnapshotOneMocked:
    def test_success_path_returns_archive_url(self):
        # Mock urlopen to return a job_id, then mock _poll_job to return success.
        spn_response = _FakeResponse({"job_id": "fake-job-id"})

        with patch("tools.snapshot.urllib.request.urlopen", return_value=spn_response), \
             patch("tools.snapshot.time.sleep"), \
             patch(
                 "tools.snapshot._poll_job",
                 return_value=("success", "https://web.archive.org/web/2026/example.com"),
             ):
            result = snapshot.snapshot_one("https://example.com", throttle_s=0)

        assert result.status == "ok"
        assert result.archive == "https://web.archive.org/web/2026/example.com"

    def test_http_401_returns_error_after_retries(self):
        import urllib.error

        # 401 → retry up to `retries` times, then return error
        def raise_401(*_args, **_kwargs):
            raise urllib.error.HTTPError(
                url="https://example.com",
                code=401,
                msg="Unauthorized",
                hdrs=None,
                fp=None,
            )

        with patch("tools.snapshot.urllib.request.urlopen", side_effect=raise_401), \
             patch("tools.snapshot.time.sleep"):
            result = snapshot.snapshot_one("https://example.com", throttle_s=0, retries=2)

        assert result.status == "error"
        assert "401" in result.reason

    def test_robots_blocked_returns_unavailable_immediately(self):
        spn_response = _FakeResponse({"job_id": "fake-job-id"})

        with patch("tools.snapshot.urllib.request.urlopen", return_value=spn_response), \
             patch("tools.snapshot.time.sleep"), \
             patch(
                 "tools.snapshot._poll_job",
                 return_value=("error", "robots.txt disallowed"),
             ):
            result = snapshot.snapshot_one("https://example.com", throttle_s=0, retries=2)

        # robots-disallowed should not retry — return unavailable
        assert result.status == "unavailable"
        assert "robots" in result.reason.lower()
