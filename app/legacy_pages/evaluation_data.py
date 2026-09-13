"""
Evaluation Data & Evidence page for Josh Talks AI evaluation.
Provides transparent data exploration, filtering, download capabilities, and consent verification.
"""

import streamlit as st
import pandas as pd
import json


def render_evaluation_data(ctx: dict):
    eval_df = ctx["evaluations_df"]
    participants_df = ctx["participants_df"]
    metrics_primary = ctx["metrics_primary"]
    sensitivity = ctx["sensitivity_check"]

    st.markdown("## 💾 EVALUATION DATA & AUDIT EVIDENCE")
    st.markdown(
        "<div style='font-size:1.0rem; color:#475569; margin-top:-8px; margin-bottom:20px;'>"
        "Direct access to normalized evaluation records, consent proof, and programmatic export tools."
        "</div>",
        unsafe_allow_html=True
    )

    data_tab1, data_tab2, data_tab3 = st.tabs([
        "1. Normalized Evaluation Records (165 Ratings)",
        "2. Participant Consent & Demographic Audit",
        "3. Data Schema & Programmatic Exports"
    ])

    with data_tab1:
        st.markdown("### Filter Normalized Evaluation Dataset")

        f1, f2, f3, f4 = st.columns(4)
        with f1:
            sel_cohort = st.selectbox("Filter Cohort:", ["All (N=11)", "Primary Only (N=10)", "11th Participant Only"])
        with f2:
            sel_model = st.selectbox("Filter Model:", ["All Models", "Model A", "Model B", "Model C"])
        with f3:
            p_names = ["All Prompts"] + sorted(eval_df["prompt_name"].unique().tolist())
            sel_prompt = st.selectbox("Filter Prompt:", p_names)
        with f4:
            p_ids = ["All Evaluators"] + sorted(eval_df["participant_id"].unique().tolist())
            sel_evaluator = st.selectbox("Filter Evaluator:", p_ids)

        filtered_df = eval_df.copy()
        if sel_cohort == "Primary Only (N=10)":
            filtered_df = filtered_df[filtered_df["is_primary_sample"] == True]
        elif sel_cohort == "11th Participant Only":
            filtered_df = filtered_df[filtered_df["is_primary_sample"] == False]

        if sel_model != "All Models":
            filtered_df = filtered_df[filtered_df["model_id"] == sel_model]
        if sel_prompt != "All Prompts":
            filtered_df = filtered_df[filtered_df["prompt_name"] == sel_prompt]
        if sel_evaluator != "All Evaluators":
            filtered_df = filtered_df[filtered_df["participant_id"] == sel_evaluator]

        st.dataframe(filtered_df, use_container_width=True, hide_index=True)
        st.caption(f"Showing {len(filtered_df)} of {len(eval_df)} total records.")

        # CSV Download button
        csv_data = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Filtered Data as CSV",
            data=csv_data,
            file_name="josh_talks_evaluations_normalized.csv",
            mime="text/csv"
        )

    with data_tab2:
        st.markdown("### Participant Consent Verification & Anonymization")
        st.markdown(
            """
            In strict compliance with privacy standards and the assignment guidelines, all personal names and email addresses have been redacted from the public application interface.
            """
        )

        st.dataframe(participants_df, use_container_width=True, hide_index=True)

        st.markdown(
            """
            <div style="background:#ECFDF5; border:1px solid #A7F3D0; border-radius:8px; padding:14px; margin-top:14px;">
                <strong style="color:#065F46;">Consent Clause Confirmed by All 11 Participants:</strong><br>
                <span style="font-size:0.85rem; color:#047857;">
                    <em>"I confirm that I am 18 years or older. I voluntarily participated in this evaluation.
                    I consent to my name, email, and responses/ratings being included in this assignment submission
                    for hiring evaluation purposes."</em>
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with data_tab3:
        st.markdown("### Data Schema Specification")
        st.markdown(
            r"""
            | Column | Type | Description |
            |---|---|---|
            | `participant_id` | String | Anonymized identifier (`P01` to `P11`) |
            | `is_primary_sample` | Boolean | True for first 10 participants ($N=10$), False for 11th |
            | `prompt_id` | String | Unique prompt key (`P1` to `P5`) |
            | `prompt_name` | String | Human-readable product category |
            | `model_id` | String | Blind evaluation model key (`Model A`, `Model B`, `Model C`) |
            | `company` | String | Commercial model developer (OpenAI, Google) |
            | `model_name` | String | Exact foundation model version |
            | `prompt_adherence` | Float | 1–5 rating for prompt following |
            | `visual_quality` | Float | 1–5 rating for sharpness & rendering fidelity |
            | `indian_authenticity`| Float | 1–5 rating for cultural & demographic plausibility |
            | `overall_score` | Float | Unweighted arithmetic mean of the three dimensions |
            | `high_rating_flag` | Boolean | True if overall score $\ge 4.0$ |
            """
        )

        st.markdown("#### Export Metrics as JSON")
        json_str = json.dumps(metrics_primary, indent=2)
        st.download_button(
            label="📥 Download Primary Benchmark JSON",
            data=json_str,
            file_name="model_metrics_primary.json",
            mime="application/json"
        )
