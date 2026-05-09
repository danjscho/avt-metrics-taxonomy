"""Pinned regression test for the worked example in README.md.

If the README's worked-example block changes its expected output
(because a function's classification bands move, or the synthetic
dataset is edited), this test fails and the diff makes the change
deliberate. Without this, the README silently drifts away from the
implementation.

The expected outputs are pinned to the live behaviour of v0.4.0 against
catalogue v5.5.12; bump them in the same commit that ships a
behaviour-changing release.
"""

from __future__ import annotations

from datetime import datetime, timedelta

import pytest

from avt_metrics_ref import (
    deployment_equity_index,
    disaggregated_wer,
    edit_rate,
    integration_error_rate,
    review_before_signing_rate,
    system_availability,
    time_to_sign_distribution,
    wer,
)


@pytest.fixture
def synthetic_week():
    g = datetime(2026, 5, 5, 9, 0)
    return {
        "asr_samples": [
            {"reference": "the patient has type two diabetes",
             "hypothesis": "the patient has type two diabetes", "group": "british-rp"},
            {"reference": "blood pressure is one forty over ninety",
             "hypothesis": "blood pressure is one forty over ninety", "group": "british-rp"},
            {"reference": "she takes metformin five hundred milligrams",
             "hypothesis": "she takes metformin five hundred milligram", "group": "scottish"},
            {"reference": "no history of cardiovascular disease",
             "hypothesis": "no history of cardiovascular disease", "group": "scottish"},
        ],
        "note_events": [
            {"clinician_id": "A", "edited": True, "edit_severity": "clinically_meaningful",
             "word_count": 220, "edit_events": 4, "scroll_events": 2, "dwell_seconds": 90,
             "generated_at": g, "approved_at": g + timedelta(seconds=120)},
            {"clinician_id": "A", "edited": True, "edit_severity": "stylistic",
             "word_count": 150, "edit_events": 1, "scroll_events": 1, "dwell_seconds": 60,
             "generated_at": g, "approved_at": g + timedelta(seconds=80)},
            {"clinician_id": "B", "edited": False,
             "word_count": 250, "edit_events": 0, "scroll_events": 0, "dwell_seconds": 4,
             "generated_at": g, "approved_at": g + timedelta(seconds=4)},
        ],
        "wb_events": (
            [{"success": True}] * 998
            + [{"success": False, "error_type": "partial", "severity": "moderate"}] * 2
        ),
        "ops_events": {"operational_minutes": 10080, "down_minutes": 30},
        "imd_to_coverage": {
            1: 0.20, 2: 0.25, 3: 0.30, 4: 0.40, 5: 0.45,
            6: 0.55, 7: 0.65, 8: 0.70, 9: 0.80, 10: 0.85,
        },
    }


def test_readme_asr_wer_pinned(synthetic_week):
    refs = [s["reference"] for s in synthetic_week["asr_samples"]]
    hyps = [s["hypothesis"] for s in synthetic_week["asr_samples"]]
    assert wer(refs, hyps) == pytest.approx(0.04166666666666667, abs=1e-9)


def test_readme_disaggregated_pinned(synthetic_week):
    result = disaggregated_wer(synthetic_week["asr_samples"], group_key="group")
    assert result["equity_gap"] == pytest.approx(0.09090909090909091, abs=1e-9)
    assert result["threshold_met"] is False


def test_readme_edit_rate_pinned(synthetic_week):
    er = edit_rate(synthetic_week["note_events"])
    # 2/3 → 66.67%, no baseline supplied
    assert er.edit_rate_pct == pytest.approx(66.66666666666666, abs=1e-9)
    assert er.classification == "no-baseline-supplied"


def test_readme_rbs_pinned(synthetic_week):
    rbs = review_before_signing_rate(synthetic_week["note_events"])
    # 2/3 reviewed (clinician B's note is 4s dwell on a 250-word note;
    # T_min = max(15, 7.5) = 15s, fails)
    assert rbs.rbs_pct == pytest.approx(66.66666666666666, abs=1e-9)
    assert rbs.classification == "pause-trigger"


def test_readme_tts_pinned(synthetic_week):
    tts = time_to_sign_distribution(synthetic_week["note_events"])
    assert tts.median_seconds == pytest.approx(80.0, abs=1e-9)
    # Clinician B's 4-second sign on a 250-word note flags both the
    # rubber-stamp threshold (TTS_norm = 0.016 << 0.5) and the
    # very-fast-on-long-note threshold (4s < 5s on > 200 words).
    assert tts.n_rubber_stamp_flag == 1
    assert tts.n_very_fast_long_note == 1


def test_readme_ier_pinned(synthetic_week):
    ier = integration_error_rate(synthetic_week["wb_events"])
    # 2 partial errors / 1000 = 0.002 → between SLA (0.001) and 5×SLA (0.005)
    assert ier.ier == pytest.approx(0.002, abs=1e-9)
    assert ier.classification == "alert-rate"


def test_readme_availability_pinned(synthetic_week):
    avail = system_availability(**synthetic_week["ops_events"])
    # (10080 - 30) / 10080 = 99.7024%; ≥ 99.5% → meets-target
    assert avail.availability_pct == pytest.approx(99.70238095238095, abs=1e-9)
    assert avail.classification == "meets-target"


def test_readme_equity_pinned(synthetic_week):
    equity = deployment_equity_index(synthetic_week["imd_to_coverage"])
    # The IMD-1-to-IMD-10 coverage curve is essentially monotonic; r ≈ 0.997.
    assert equity.pearson_r > 0.99
    assert equity.direction == "inequity"
    assert equity.classification == "inequity-flagged"
