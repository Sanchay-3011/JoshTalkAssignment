"""
Data cleaning and normalization script for Josh Talks AI evaluation.
Converts wide Google Forms responses into a clean, normalized, long-format schema
while rigorously anonymizing participant PII and applying the 10-primary / 11-robustness protocol.
"""

import os
import re
import pandas as pd
import numpy as np


RAW_DATA_PATH = os.path.join("data", "raw", "form_responses.csv")
NORMALIZED_DATA_PATH = os.path.join("data", "processed", "evaluations_normalized.csv")
PARTICIPANTS_PATH = os.path.join("data", "processed", "participants_anonymized.csv")

# Prompt metadata mapping matching column blocks in the CSV
PROMPT_BLOCKS = [
    {
        "prompt_id": "P1",
        "prompt_name": "Red Banarasi Silk Saree",
        "start_col": 6,
        "folder": "Prompt1"
    },
    {
        "prompt_id": "P2",
        "prompt_name": "Stainless Steel Tiffin Box",
        "start_col": 16,
        "folder": "Prompt2"
    },
    {
        "prompt_id": "P3",
        "prompt_name": "Festive Namkeen Snack Pouch",
        "start_col": 26,
        "folder": "Prompt4"
    },
    {
        "prompt_id": "P4",
        "prompt_name": "Beige Cotton Kurta Set",
        "start_col": 36,
        "folder": "Prompt3"
    },
    {
        "prompt_id": "P5",
        "prompt_name": "Navy Blue Nehru Jacket",
        "start_col": 46,
        "folder": "Prompt5"
    }
]

MODELS = [
    {"model_id": "Model A", "offset": 0, "company": "OpenAI", "model_name": "ChatGPT Images 2.5"},
    {"model_id": "Model B", "offset": 3, "company": "Google", "model_name": "Gemini 3.1 Pro Image"},
    {"model_id": "Model C", "offset": 6, "company": "Google", "model_name": "Gemini 3.5 Flash-Lite"}
]


def clean_and_normalize(raw_path: str = RAW_DATA_PATH) -> pd.DataFrame:
    """Read wide raw survey data and transform to normalized long format."""
    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Raw responses file not found at {raw_path}")

    df_raw = pd.read_csv(raw_path)
    num_rows = len(df_raw)

    evaluations = []
    participants = []

    for idx, row in df_raw.iterrows():
        p_num = idx + 1
        participant_id = f"P{p_num:02d}"
        is_primary = (p_num <= 10)

        # Basic demographics (anonymized)
        age = int(row["Age"]) if pd.notna(row["Age"]) else None
        timestamp = str(row["Timestamp"])
        consent_text = str(row["Consent"])
        consent_verified = "consent to my name, email, and responses" in consent_text

        participants.append({
            "participant_id": participant_id,
            "age": age,
            "timestamp": timestamp,
            "consent_verified": consent_verified,
            "is_primary_sample": is_primary
        })

        for p_block in PROMPT_BLOCKS:
            prompt_id = p_block["prompt_id"]
            prompt_name = p_block["prompt_name"]
            start_col = p_block["start_col"]

            for m in MODELS:
                model_id = m["model_id"]
                offset = m["offset"]

                # 3 criteria per image
                pa_val = float(row.iloc[start_col + offset])
                vq_val = float(row.iloc[start_col + offset + 1])
                ia_val = float(row.iloc[start_col + offset + 2])

                overall = round((pa_val + vq_val + ia_val) / 3.0, 4)
                high_rating = bool(overall >= 4.0)

                evaluations.append({
                    "participant_id": participant_id,
                    "is_primary_sample": is_primary,
                    "prompt_id": prompt_id,
                    "prompt_name": prompt_name,
                    "model_id": model_id,
                    "company": m["company"],
                    "model_name": m["model_name"],
                    "prompt_adherence": pa_val,
                    "visual_quality": vq_val,
                    "indian_authenticity": ia_val,
                    "overall_score": overall,
                    "high_rating_flag": high_rating
                })

    df_evals = pd.DataFrame(evaluations)
    df_participants = pd.DataFrame(participants)

    os.makedirs(os.path.dirname(NORMALIZED_DATA_PATH), exist_ok=True)
    df_evals.to_csv(NORMALIZED_DATA_PATH, index=False)
    df_participants.to_csv(PARTICIPANTS_PATH, index=False)

    print(f"Successfully processed {num_rows} survey rows into {len(df_evals)} evaluation records.")
    print(f"Saved normalized data to: {NORMALIZED_DATA_PATH}")
    print(f"Saved anonymized participants to: {PARTICIPANTS_PATH}")

    return df_evals


if __name__ == "__main__":
    clean_and_normalize()
