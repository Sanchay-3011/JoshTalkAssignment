"""
Unit tests for data pipeline, anonymization, and schema integrity.
"""

import os
import pandas as pd
import pytest

RAW_PATH = os.path.join("data", "raw", "form_responses.csv")
NORMALIZED_PATH = os.path.join("data", "processed", "evaluations_normalized.csv")
PARTICIPANTS_PATH = os.path.join("data", "processed", "participants_anonymized.csv")


def test_raw_data_exists_and_has_11_records():
    assert os.path.exists(RAW_PATH), "Raw survey responses file is missing"
    df_raw = pd.read_csv(RAW_PATH)
    assert len(df_raw) == 11, f"Expected 11 raw responses, found {len(df_raw)}"


def test_normalized_data_shape_and_counts():
    assert os.path.exists(NORMALIZED_PATH), "Normalized evaluation file is missing"
    df = pd.read_csv(NORMALIZED_PATH)
    # 11 participants x 5 prompts x 3 models = 165 evaluation rows
    assert len(df) == 165, f"Expected 165 normalized rows, found {len(df)}"

    primary_df = df[df["is_primary_sample"] == True]
    # 10 primary participants x 5 prompts x 3 models = 150 rows
    assert len(primary_df) == 150, f"Expected 150 primary rows, found {len(primary_df)}"

    robust_11th_df = df[df["is_primary_sample"] == False]
    # 1 participant x 5 prompts x 3 models = 15 rows
    assert len(robust_11th_df) == 15, f"Expected 15 rows for 11th participant, found {len(robust_11th_df)}"


def test_pii_anonymization():
    """Ensure participant emails and personal names are excluded from public normalized datasets."""
    df = pd.read_csv(NORMALIZED_PATH)
    forbidden_columns = ["Email", "Full Name", "email", "name", "Full_Name"]
    for col in forbidden_columns:
        assert col not in df.columns, f"PII column '{col}' detected in normalized dataset"

    # Verify participant IDs are formatted as P01..P11
    p_ids = df["participant_id"].unique()
    assert len(p_ids) == 11
    for pid in p_ids:
        assert pid.startswith("P"), f"Invalid anonymized participant ID: {pid}"


def test_consent_verification():
    """Ensure all participants gave affirmative consent."""
    assert os.path.exists(PARTICIPANTS_PATH)
    df_p = pd.read_csv(PARTICIPANTS_PATH)
    assert len(df_p) == 11
    assert df_p["consent_verified"].all(), "Not all participants have verified consent"
    assert (df_p["age"] >= 18).all(), "All participants must be 18 years or older"
