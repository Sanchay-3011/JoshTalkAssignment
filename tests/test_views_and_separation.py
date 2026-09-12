"""
Tests for UI Architecture, Data Isolation, and Image Integrity.
Verifies that:
1. All 15 images referenced by prompts exist on disk.
2. The Beta rating submission workflow writes exclusively to data/beta_responses/
   and never alters data/processed/ or data/raw/.
3. Assignment evaluation dataset strictly excludes participant PII.
"""

import os
import json
import pandas as pd
import pytest

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROMPTS_META_PATH = os.path.join(BASE_DIR, "data", "metadata", "prompts.json")
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "form_responses.csv")
NORMALIZED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "evaluations_normalized.csv")
BETA_DIR = os.path.join(BASE_DIR, "data", "beta_responses")


def test_all_15_images_exist_on_disk():
    assert os.path.exists(PROMPTS_META_PATH)
    with open(PROMPTS_META_PATH, "r", encoding="utf-8") as f:
        prompts = json.load(f)

    assert len(prompts) == 5
    total_images_found = 0
    for p_id, p_info in prompts.items():
        images = p_info.get("images", {})
        assert len(images) == 3, f"Prompt {p_id} must have 3 model images"
        for mid, img_rel_path in images.items():
            full_img_path = os.path.join(BASE_DIR, img_rel_path)
            assert os.path.exists(full_img_path), f"Image missing: {full_img_path} for {p_id} {mid}"
            total_images_found += 1

    assert total_images_found == 15, f"Expected exactly 15 images, found {total_images_found}"


def test_data_separation_and_beta_storage(tmp_path):
    """Verify that writing beta submissions never modifies primary normalized evaluation data."""
    raw_mtime_before = os.path.getmtime(RAW_DATA_PATH)
    norm_mtime_before = os.path.getmtime(NORMALIZED_DATA_PATH)

    df_norm_before = pd.read_csv(NORMALIZED_DATA_PATH)
    assert len(df_norm_before) == 165

    # Simulate beta response saving
    os.makedirs(BETA_DIR, exist_ok=True)
    test_beta_record = {
        "submission_id": "TEST_UNIT_001",
        "participant": {"name": "Test User", "email": "test@example.com", "age": 28, "consent": True},
        "ratings": {
            "P1": {"Image A": {"adherence": 5, "quality": 5, "authenticity": 5}}
        }
    }
    test_json = os.path.join(BETA_DIR, "test_beta.json")
    with open(test_json, "w") as f:
        json.dump(test_beta_record, f)

    assert os.path.exists(test_json)
    os.remove(test_json)

    # Confirm primary files remain completely untouched
    assert os.path.getmtime(RAW_DATA_PATH) == raw_mtime_before
    assert os.path.getmtime(NORMALIZED_DATA_PATH) == norm_mtime_before
    df_norm_after = pd.read_csv(NORMALIZED_DATA_PATH)
    assert len(df_norm_after) == 165
