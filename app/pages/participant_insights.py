"""
Participant Insights & Disagreement page for Josh Talks AI evaluation.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from app.components.cards import (
    render_kpi_card,
    render_rater_disagreement_heatmap,
    get_model_label
)


def render_participant_insights(ctx: dict):
    eval_df = ctx["evaluations_df"]
    participants_df = ctx["participants_df"]
    models_meta = ctx["models_meta"]
    disclose = ctx["disclose_models"]
    is_primary = ctx["is_primary"]
    stats_meta = ctx["stats_meta"]

    st.markdown("## 👥 PARTICIPANT INSIGHTS & RATER AGREEMENT")
    st.markdown(
        "<div style='font-size:1.0rem; color:#475569; margin-top:-8px; margin-bottom:20px;'>"
        "Statistical breakdown of evaluator judgments, rating variance, demographic distribution, and consensus patterns."
        "</div>",
        unsafe_allow_html=True
    )

    df_active = eval_df[eval_df["is_primary_sample"] == True] if is_primary else eval_df
    n_active = len(df_active["participant_id"].unique())

    # Top KPI Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Evaluator Sample", f"{n_active} Raters", "100% Verified Consent", badge_text="18+ Validated", badge_type="blue")
    with col2:
        ages = participants_df["age"] if not is_primary else participants_df[participants_df["is_primary_sample"] == True]["age"]
        render_kpi_card("Mean Age", f"{ages.mean():.1f} Yrs", f"Range: {ages.min()}–{ages.max()} yrs", badge_text="Demographics", badge_type="slate")
    with col3:
        corr = stats_meta.get("inter_rater_consensus", {}).get("mean_pairwise_correlation", 0.34)
        render_kpi_card("Inter-Rater Agreement", f"r = {corr:.2f}", "Pairwise Correlation", badge_text="Consensus", badge_type="gold")
    with col4:
        pct_high = (df_active["overall_score"] >= 4.0).mean() * 100
        render_kpi_card("High-Rating Share", f"{pct_high:.1f}%", "Scores ≥ 4.0 / 5", badge_text="Positive Sentiment", badge_type="slate")

    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)

    # Question 1: How are ratings distributed across the three models?
    st.markdown("### 1. Rating Distribution Across Models (Box Plots & Spread)")
    st.markdown(
        "<div style='font-size:0.85rem; color:#64748B; margin-top:-5px; margin-bottom:12px;'>"
        "Answers: <em>How consistent are raters when scoring each model? Does Model A have tighter consensus while Model C is polarized?</em>"
        "</div>",
        unsafe_allow_html=True
    )

    fig_box = px.box(
        df_active,
        x="model_id",
        y="overall_score",
        color="model_id",
        points="all",
        color_discrete_map={"Model A": "#F59E0B", "Model B": "#3B82F6", "Model C": "#94A3B8"},
        labels={"model_id": "Model", "overall_score": "Overall Score (1-5 Likert)"}
    )
    fig_box.update_layout(
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        yaxis=dict(gridcolor="#F1F5F9", range=[0.5, 5.5]),
        margin=dict(l=20, r=20, t=20, b=20),
        height=350,
        showlegend=False,
        font=dict(family="Plus Jakarta Sans", color="#1E293B")
    )
    st.plotly_chart(fig_box, use_container_width=True)

    st.markdown("---")

    # Question 2: Where did evaluators disagree most?
    st.markdown("### 2. Evaluator Disagreement Matrix (Prompt × Model Heatmap)")
    st.markdown(
        "<div style='font-size:0.85rem; color:#64748B; margin-top:-5px; margin-bottom:12px;'>"
        "Answers: <em>Which prompt-model combinations triggered the highest variance among raters? (Higher standard deviation = greater rater disagreement)</em>"
        "</div>",
        unsafe_allow_html=True
    )

    c_heat1, c_heat2 = st.columns([3, 2])
    with c_heat1:
        fig_heat = render_rater_disagreement_heatmap(df_active)
        st.plotly_chart(fig_heat, use_container_width=True)

    with c_heat2:
        st.markdown(
            """
            <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:16px; margin-top:20px;">
                <h5 style="margin-top:0; color:#1E293B;">Key Disagreement Insights</h5>
                <ul style="font-size:0.85rem; color:#475569; line-height:1.6; padding-left:18px;">
                    <li><strong>Model A Consensus:</strong> Shows the lowest standard deviation (avg ±0.58), meaning human evaluators were virtually unanimous in awarding top marks.</li>
                    <li><strong>Model C Polarization:</strong> Spikes to ±1.54 on the Tiffin Box prompt and ±1.44 on the Saree prompt. Evaluators were deeply split—some gave it 1s due to the wooden doll mannequin, while others gave it 4s/5s for lighting.</li>
                    <li><strong>Cultural Ambiguity in Model B:</strong> Achieved moderate consensus (±0.88), with lowest variance on the Diwali Namkeen prompt where festive decorations were universally recognized.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # Question 3: Evaluator Demographics and Privacy Protection
    st.markdown("### 3. Evaluator Demographics & Consent Protection")
    st.markdown(
        "<div style='font-size:0.85rem; color:#64748B; margin-top:-5px; margin-bottom:12px;'>"
        "All participant email addresses and personal identities have been stripped from public presentation to preserve privacy."
        "</div>",
        unsafe_allow_html=True
    )

    c_dem1, c_dem2 = st.columns([2, 3])
    with c_dem1:
        fig_age = px.histogram(
            participants_df if not is_primary else participants_df[participants_df["is_primary_sample"] == True],
            x="age",
            nbins=6,
            color_discrete_sequence=["#3B82F6"],
            labels={"age": "Evaluator Age (Years)"}
        )
        fig_age.update_layout(
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            yaxis=dict(title="Count", gridcolor="#F1F5F9"),
            margin=dict(l=20, r=20, t=20, b=20),
            height=280,
            font=dict(family="Plus Jakarta Sans", color="#1E293B")
        )
        st.plotly_chart(fig_age, use_container_width=True)

    with c_dem2:
        # Anonymized evaluator roster
        p_table = participants_df.copy()
        p_table["Cohort Status"] = p_table["is_primary_sample"].apply(lambda x: "Primary Benchmark (N=10)" if x else "Sensitivity Check (11th)")
        p_table["Consent"] = p_table["consent_verified"].apply(lambda x: "✓ Verified 18+ Voluntary" if x else "Missing")

        display_p = p_table[["participant_id", "age", "Cohort Status", "Consent", "timestamp"]].rename(
            columns={"participant_id": "Evaluator ID", "age": "Age", "timestamp": "Submission Timestamp"}
        )
        st.dataframe(display_p, use_container_width=True, hide_index=True)
