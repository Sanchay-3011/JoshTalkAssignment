"""
Unit tests for metric accuracy, score reproducibility, and ranking stability.
"""

import json
import os
import pytest

PRIMARY_METRICS_PATH = os.path.join("data", "processed", "model_metrics_primary.json")
ROBUSTNESS_METRICS_PATH = os.path.join("data", "processed", "model_metrics_robustness.json")
SENSITIVITY_PATH = os.path.join("data", "processed", "sensitivity_check.json")


@pytest.fixture
def primary_metrics():
    assert os.path.exists(PRIMARY_METRICS_PATH)
    with open(PRIMARY_METRICS_PATH, "r") as f:
        return json.load(f)


@pytest.fixture
def robustness_metrics():
    assert os.path.exists(ROBUSTNESS_METRICS_PATH)
    with open(ROBUSTNESS_METRICS_PATH, "r") as f:
        return json.load(f)


@pytest.fixture
def sensitivity_report():
    assert os.path.exists(SENSITIVITY_PATH)
    with open(SENSITIVITY_PATH, "r") as f:
        return json.load(f)


def test_primary_metrics_accuracy(primary_metrics):
    """Verify calculated metrics match source observed data within tolerance."""
    # Model A: ~4.73 overall, ~4.78 pa, ~4.74 vq, ~4.68 ia
    mA = primary_metrics["Model A"]
    assert pytest.approx(mA["overall_score"], abs=0.05) == 4.73
    assert pytest.approx(mA["prompt_adherence_mean"], abs=0.05) == 4.78
    assert pytest.approx(mA["visual_quality_mean"], abs=0.05) == 4.74
    assert pytest.approx(mA["indian_authenticity_mean"], abs=0.05) == 4.68
    assert mA["rank"] == 1

    # Model B: ~3.76 overall, ~3.76 pa, ~3.72 vq, ~3.80 ia
    mB = primary_metrics["Model B"]
    assert pytest.approx(mB["overall_score"], abs=0.05) == 3.76
    assert pytest.approx(mB["prompt_adherence_mean"], abs=0.05) == 3.76
    assert pytest.approx(mB["visual_quality_mean"], abs=0.05) == 3.72
    assert pytest.approx(mB["indian_authenticity_mean"], abs=0.05) == 3.80
    assert mB["rank"] == 2

    # Model C: ~3.29 overall, ~3.28 pa, ~3.30 vq, ~3.28 ia
    mC = primary_metrics["Model C"]
    assert pytest.approx(mC["overall_score"], abs=0.05) == 3.29
    assert pytest.approx(mC["prompt_adherence_mean"], abs=0.05) == 3.28
    assert pytest.approx(mC["visual_quality_mean"], abs=0.05) == 3.30
    assert pytest.approx(mC["indian_authenticity_mean"], abs=0.05) == 3.28
    assert mC["rank"] == 3


def test_ranking_hierarchy_and_stability(primary_metrics, robustness_metrics, sensitivity_report):
    """Ensure Model A > Model B > Model C holds across both sample regimes."""
    assert primary_metrics["Model A"]["overall_score"] > primary_metrics["Model B"]["overall_score"]
    assert primary_metrics["Model B"]["overall_score"] > primary_metrics["Model C"]["overall_score"]

    assert robustness_metrics["Model A"]["overall_score"] > robustness_metrics["Model B"]["overall_score"]
    assert robustness_metrics["Model B"]["overall_score"] > robustness_metrics["Model C"]["overall_score"]

    assert sensitivity_report["rank_unchanged"] is True


def test_high_rating_percentage(primary_metrics):
    """Model A should have significantly higher 4-5 rating percentage than B and C."""
    mA_pct = primary_metrics["Model A"]["high_rating_percentage"]
    mB_pct = primary_metrics["Model B"]["high_rating_percentage"]
    mC_pct = primary_metrics["Model C"]["high_rating_percentage"]

    assert mA_pct > 85.0
    assert mB_pct > 50.0
    assert mA_pct > mB_pct > mC_pct
