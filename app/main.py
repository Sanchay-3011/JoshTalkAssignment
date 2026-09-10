"""
Main entrypoint for Josh Talks AI: India E-Commerce Text-to-Image Model Evaluation Platform.
Production-grade dashboard presenting human-in-the-loop benchmarks across OpenAI and Google models.
"""

import os
import sys

# Ensure repository root is on sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
if os.path.dirname(__file__) not in sys.path:
    sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
import pandas as pd
from app.config import (
    apply_custom_css,
    load_evaluations,
    load_participants,
    load_models_metadata,
    load_prompts_metadata,
    load_qualitative_notes,
    load_model_metrics_primary,
    load_model_metrics_robustness,
    load_prompt_metrics,
    load_sensitivity_check,
    load_statistical_analysis
)

# Set page configuration
st.set_page_config(
    page_title="India E-Commerce Image Evaluation | Josh Talks AI",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom design tokens
apply_custom_css()

# Load all cached data
evaluations_df = load_evaluations()
participants_df = load_participants()
models_meta = load_models_metadata()
prompts_meta = load_prompts_metadata()
qualitative_notes = load_qualitative_notes()
metrics_primary = load_model_metrics_primary()
metrics_robustness = load_model_metrics_robustness()
prompt_metrics = load_prompt_metrics()
sensitivity_check = load_sensitivity_check()
stats_meta = load_statistical_analysis()

# Sidebar Setup
with st.sidebar:
    st.markdown("### 🇮🇳 Josh Talks AI")
    st.markdown(
        "<div style='font-size:0.8rem; color:#64748B; margin-top:-10px; margin-bottom:15px;'>"
        "Text-to-Image Benchmark Engine · Indian E-Commerce"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown("#### ⚙️ Evaluation Controls")

    # Blinding Toggle
    disclose_models = st.toggle(
        "Disclose Model Identities",
        value=True,
        help="Toggle between blind evaluation labels (Model A, B, C) and disclosed provider names (OpenAI, Google Gemini)."
    )

    # Sample Selection Toggle
    sample_choice = st.radio(
        "Participant Cohort",
        ["Primary Benchmark (N=10)", "Sensitivity / Robustness (N=11)"],
        index=0,
        help="Primary benchmark conforms strictly to the 8-10 participant protocol. The 11th participant is retained for sensitivity verification."
    )
    is_primary = (sample_choice == "Primary Benchmark (N=10)")
    active_metrics = metrics_primary if is_primary else metrics_robustness

    st.markdown("---")
    st.markdown("#### 📑 Navigation")
    pages = [
        "1. Executive Overview",
        "2. Model Leaderboard",
        "3. Prompt-Level Analysis",
        "4. Side-by-Side Image Inspector",
        "5. Participant Insights & Disagreement",
        "6. Methodology & Fairness",
        "7. Raw Evaluation Data & Evidence",
        "8. Human Evaluation Rating UI (Product Concept)",
        "9. Scaling Proposal & Architecture",
        "10. Final Reports & Reflection"
    ]
    selected_page = st.radio("Go to Page:", pages, label_visibility="collapsed")

    st.markdown("---")
    st.markdown("#### 📊 Evaluation Specs")
    st.markdown(
        """
        - **Domain:** Indian E-Commerce
        - **Use Case:** Catalog & Festive Ads
        - **Prompts:** 5 Curated Categories
        - **Generated Images:** 15 Original PNGs
        - **Total Ratings:** 165 Criteria Points
        - **Scale:** 1–5 Likert Dimensions
        """
    )
    st.markdown(
        "<div style='font-size:0.75rem; color:#94A3B8; margin-top:20px;'>"
        "Josh Talks AI · Product Operations Evaluation"
        "</div>",
        unsafe_allow_html=True
    )

# Page Dispatcher
context = {
    "evaluations_df": evaluations_df,
    "participants_df": participants_df,
    "models_meta": models_meta,
    "prompts_meta": prompts_meta,
    "qualitative_notes": qualitative_notes,
    "metrics": active_metrics,
    "metrics_primary": metrics_primary,
    "metrics_robustness": metrics_robustness,
    "prompt_metrics": prompt_metrics,
    "sensitivity_check": sensitivity_check,
    "stats_meta": stats_meta,
    "disclose_models": disclose_models,
    "is_primary": is_primary
}

if selected_page == "1. Executive Overview":
    from app.pages.overview import render_overview
    render_overview(context)
elif selected_page == "2. Model Leaderboard":
    from app.pages.leaderboard import render_leaderboard
    render_leaderboard(context)
elif selected_page == "3. Prompt-Level Analysis":
    from app.pages.prompt_analysis import render_prompt_analysis
    render_prompt_analysis(context)
elif selected_page == "4. Side-by-Side Image Inspector":
    from app.pages.image_comparison import render_image_comparison
    render_image_comparison(context)
elif selected_page == "5. Participant Insights & Disagreement":
    from app.pages.participant_insights import render_participant_insights
    render_participant_insights(context)
elif selected_page == "6. Methodology & Fairness":
    from app.pages.methodology import render_methodology
    render_methodology(context)
elif selected_page == "7. Raw Evaluation Data & Evidence":
    from app.pages.evaluation_data import render_evaluation_data
    render_evaluation_data(context)
elif selected_page == "8. Human Evaluation Rating UI (Product Concept)":
    from app.pages.rating_ui_concept import render_rating_ui_concept
    render_rating_ui_concept(context)
elif selected_page == "9. Scaling Proposal & Architecture":
    from app.pages.scaling_plan import render_scaling_plan
    render_scaling_plan(context)
elif selected_page == "10. Final Reports & Reflection":
    from app.pages.reports_page import render_reports_page
    render_reports_page(context)
