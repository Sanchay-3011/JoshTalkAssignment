"""
Score calculation engine for Josh Talks AI evaluation.
Computes primary benchmark scores (first 10 participants),
sensitivity / robustness metrics (all 11 participants),
prompt-level breakdowns, and rating distributions.
"""

import json
import os
import pandas as pd
import numpy as np

NORMALIZED_PATH = os.path.join("data", "processed", "evaluations_normalized.csv")
PRIMARY_OUTPUT_JSON = os.path.join("data", "processed", "model_metrics_primary.json")
ROBUSTNESS_OUTPUT_JSON = os.path.join("data", "processed", "model_metrics_robustness.json")
PROMPT_OUTPUT_JSON = os.path.join("data", "processed", "prompt_metrics.json")
SENSITIVITY_OUTPUT_JSON = os.path.join("data", "processed", "sensitivity_check.json")


def compute_model_metrics(df_subset: pd.DataFrame) -> dict:
    """Compute comprehensive aggregated metrics for models in a given dataframe subset."""
    models = ["Model A", "Model B", "Model C"]
    metrics = {}

    for model_id in models:
        m_df = df_subset[df_subset["model_id"] == model_id]

        overall_scores = m_df["overall_score"].values
        pa_scores = m_df["prompt_adherence"].values
        vq_scores = m_df["visual_quality"].values
        ia_scores = m_df["indian_authenticity"].values

        # Ratings 4 or 5 count across all 3 criteria (or overall)
        all_ratings = np.concatenate([pa_scores, vq_scores, ia_scores])
        high_rating_pct = round(float(np.mean(all_ratings >= 4.0) * 100), 2)

        # Standard deviation as measure of disagreement/consistency
        std_overall = float(np.std(overall_scores, ddof=1)) if len(overall_scores) > 1 else 0.0
        consistency_score = round(float(1.0 / (1.0 + std_overall)), 3)

        company = m_df["company"].iloc[0] if "company" in m_df.columns else "Unknown"
        model_name = m_df["model_name"].iloc[0] if "model_name" in m_df.columns else model_id

        metrics[model_id] = {
            "model_id": model_id,
            "company": company,
            "model_name": model_name,
            "sample_size": len(m_df["participant_id"].unique()),
            "total_ratings": len(overall_scores),
            "overall_score": round(float(np.mean(overall_scores)), 3),
            "overall_median": round(float(np.median(overall_scores)), 3),
            "overall_std": round(std_overall, 3),
            "prompt_adherence_mean": round(float(np.mean(pa_scores)), 3),
            "prompt_adherence_median": round(float(np.median(pa_scores)), 3),
            "prompt_adherence_std": round(float(np.std(pa_scores, ddof=1)), 3),
            "visual_quality_mean": round(float(np.mean(vq_scores)), 3),
            "visual_quality_median": round(float(np.median(vq_scores)), 3),
            "visual_quality_std": round(float(np.std(vq_scores, ddof=1)), 3),
            "indian_authenticity_mean": round(float(np.mean(ia_scores)), 3),
            "indian_authenticity_median": round(float(np.median(ia_scores)), 3),
            "indian_authenticity_std": round(float(np.std(ia_scores, ddof=1)), 3),
            "high_rating_percentage": high_rating_pct,
            "consistency_index": consistency_score
        }

    # Add Rank
    ranked = sorted(metrics.values(), key=lambda x: x["overall_score"], reverse=True)
    for rank_idx, m in enumerate(ranked):
        metrics[m["model_id"]]["rank"] = rank_idx + 1

    return metrics


def compute_prompt_metrics(df_subset: pd.DataFrame) -> dict:
    """Compute prompt-level metrics per model."""
    prompts = sorted(df_subset["prompt_id"].unique())
    models = ["Model A", "Model B", "Model C"]
    prompt_res = {}

    for pid in prompts:
        p_df = df_subset[df_subset["prompt_id"] == pid]
        p_name = p_df["prompt_name"].iloc[0]
        prompt_res[pid] = {
            "prompt_id": pid,
            "prompt_name": p_name,
            "models": {}
        }

        for mid in models:
            m_df = p_df[p_df["model_id"] == mid]
            pa = m_df["prompt_adherence"].values
            vq = m_df["visual_quality"].values
            ia = m_df["indian_authenticity"].values
            ov = m_df["overall_score"].values

            prompt_res[pid]["models"][mid] = {
                "overall": round(float(np.mean(ov)), 3),
                "overall_std": round(float(np.std(ov, ddof=1)), 3) if len(ov) > 1 else 0.0,
                "prompt_adherence": round(float(np.mean(pa)), 3),
                "visual_quality": round(float(np.mean(vq)), 3),
                "indian_authenticity": round(float(np.mean(ia)), 3),
                "ratings_count": len(ov),
                "score_distribution": {
                    str(score): int(np.sum(np.round(ov) == score)) for score in range(1, 6)
                }
            }

    return prompt_res


def run_pipeline():
    df = pd.read_csv(NORMALIZED_PATH)

    # 1. Primary Analysis (N=10)
    df_primary = df[df["is_primary_sample"] == True]
    primary_metrics = compute_model_metrics(df_primary)
    primary_prompts = compute_prompt_metrics(df_primary)

    # 2. Robustness Analysis (N=11)
    robustness_metrics = compute_model_metrics(df)
    robustness_prompts = compute_prompt_metrics(df)

    # 3. Sensitivity Comparison
    primary_ranks = {k: v["rank"] for k, v in primary_metrics.items()}
    robustness_ranks = {k: v["rank"] for k, v in robustness_metrics.items()}
    rank_unchanged = (primary_ranks == robustness_ranks)

    deltas = {}
    for mid in ["Model A", "Model B", "Model C"]:
        p_score = primary_metrics[mid]["overall_score"]
        r_score = robustness_metrics[mid]["overall_score"]
        deltas[mid] = {
            "primary_score": p_score,
            "robustness_score": r_score,
            "delta": round(r_score - p_score, 4),
            "primary_rank": primary_ranks[mid],
            "robustness_rank": robustness_ranks[mid]
        }

    sensitivity_report = {
        "rank_unchanged": rank_unchanged,
        "summary": "The model ranking was unchanged when the additional response was included." if rank_unchanged else "Ranking altered.",
        "deltas": deltas,
        "primary_sample_size": 10,
        "robustness_sample_size": 11
    }

    # Save to disk
    with open(PRIMARY_OUTPUT_JSON, "w") as f:
        json.dump(primary_metrics, f, indent=2)
    with open(ROBUSTNESS_OUTPUT_JSON, "w") as f:
        json.dump(robustness_metrics, f, indent=2)
    with open(PROMPT_OUTPUT_JSON, "w") as f:
        json.dump(primary_prompts, f, indent=2)
    with open(SENSITIVITY_OUTPUT_JSON, "w") as f:
        json.dump(sensitivity_report, f, indent=2)

    print("Primary Model Metrics (N=10):")
    for mid, data in primary_metrics.items():
        print(f"  {mid} (Rank {data['rank']}): Overall={data['overall_score']}, Adherence={data['prompt_adherence_mean']}, Visual={data['visual_quality_mean']}, Authenticity={data['indian_authenticity_mean']}, HighRating%={data['high_rating_percentage']}%")

    print("\nRobustness Check (N=11):")
    print(f"  Rank unchanged: {rank_unchanged}")
    for mid, d in deltas.items():
        print(f"  {mid}: Primary={d['primary_score']} -> Robustness={d['robustness_score']} (Delta={d['delta']:+0.3f})")


if __name__ == "__main__":
    run_pipeline()
