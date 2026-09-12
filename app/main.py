"""
India Image Eval: Human Evaluation of Text-to-Image Foundation Models for Indian E-Commerce.
Main entrypoint for the streamlined Streamlit product experience.
Architecture:
  HOME
   ├── 📊 Assignment Evaluation (Single unified executive report)
   └── 🧪 Try Rating App (Beta participant rating prototype)
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

from app.views.home import render_home
from app.views.results import render_assignment_results
from app.views.rating_app import render_try_rating_app


# Page Configuration
st.set_page_config(
    page_title="India Image Eval · Text-to-Image Benchmark",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply global design system CSS
apply_custom_css()

# Initialize Session State
if "view" not in st.session_state:
    st.session_state["view"] = "home"

# Load cached evaluation datasets
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

# Context dictionary passed to views
context = {
    "evaluations_df": evaluations_df,
    "participants_df": participants_df,
    "models_meta": models_meta,
    "prompts_meta": prompts_meta,
    "qualitative_notes": qualitative_notes,
    "metrics_primary": metrics_primary,
    "metrics_robustness": metrics_robustness,
    "prompt_metrics": prompt_metrics,
    "sensitivity_check": sensitivity_check,
    "stats_meta": stats_meta,
    "disclose_models": True,
    "is_primary": True
}

# Sidebar: Concise, purposeful navigation & product info
with st.sidebar:
    st.markdown(
        """
        <div style="margin-bottom: 15px;">
            <div style="font-size: 1.15rem; font-weight: 800; color: #0F172A; letter-spacing: -0.02em;">
                🇮🇳 INDIA IMAGE EVAL
            </div>
            <div style="font-size: 0.78rem; color: #64748B; margin-top: 2px;">
                Text-to-Image Evaluation Platform
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown("#### 🧭 Navigation")

    current_view = st.session_state.get("view", "home")

    if current_view != "home":
        if st.button("🏠 Return to Homepage", key="sidebar_btn_home", use_container_width=True):
            st.session_state["view"] = "home"
            st.rerun()

    if st.button("📊 Assignment Evaluation", key="sidebar_btn_results", use_container_width=True, type="primary" if current_view == "assignment_results" else "secondary"):
        st.session_state["view"] = "assignment_results"
        st.rerun()

    if st.button("🧪 Try Rating App (Beta)", key="sidebar_btn_beta", use_container_width=True, type="primary" if current_view == "try_rating_app" else "secondary"):
        st.session_state["view"] = "try_rating_app"
        st.rerun()

    st.markdown("---")
    st.markdown("#### ℹ️ Project Scope")
    st.markdown(
        """
        - **Domain:** Indian E-Commerce
        - **Use Case:** Catalog & Festive Ads
        - **Foundation Models:** 3 Evaluated
        - **Curated Prompts:** 5 Categories
        - **Evaluator Sample:** 10 Primary ($N=10$) + 1 Robustness ($N=11$)
        - **Rating Dimensions:** 3 Orthogonal Criteria
        """
    )

    st.markdown(
        """
        <div style="font-size: 0.74rem; color: #94A3B8; margin-top: 30px;">
            Josh Talks AI · Product Operations Task
        </div>
        """,
        unsafe_allow_html=True
    )


# Primary View Dispatcher
if st.session_state["view"] == "home":
    render_home()
elif st.session_state["view"] == "assignment_results":
    render_assignment_results(context)
elif st.session_state["view"] == "try_rating_app":
    render_try_rating_app(context)
else:
    render_home()
