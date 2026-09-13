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

# Sidebar matching exact reference design
with st.sidebar:
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 22px;">
            <svg width="38" height="38" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M5 12C12 8 26 16 35 12V18C26 22 12 14 5 18V12Z" fill="#FF9933"/>
                <path d="M5 18C12 14 26 22 35 18V24C26 28 12 20 5 24V18Z" fill="#FFFFFF"/>
                <path d="M5 24C12 20 26 28 35 24V30C26 34 12 26 5 30V24Z" fill="#138808"/>
                <circle cx="20" cy="21" r="2.6" stroke="#000080" stroke-width="0.8" fill="none"/>
            </svg>
            <div>
                <div style="font-size: 1.05rem; font-weight: 800; color: #0F172A; letter-spacing: -0.01em; line-height: 1.2;">
                    INDIA IMAGE EVAL
                </div>
                <div style="font-size: 0.74rem; color: #64748B; margin-top: 2px;">
                    Text-to-Image Evaluation Platform
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    current_view = st.session_state.get("view", "home")

    # Nav Home Card Button
    if st.button("Home", key="sidebar_nav_home", use_container_width=True):
        st.session_state["view"] = "home"
        st.rerun()

    st.markdown(
        """
        <div style="font-size: 0.82rem; color: #64748B; line-height: 1.5; margin: 16px 0 20px 0;">
            Human evaluation of image generation models for Indian e-commerce.
        </div>
        <hr style="border: none; border-top: 1px solid #E2E8F0; margin: 0 0 20px 0;">
        <div style="
            background: #F1F5F9;
            border: 1px solid #E2E8F0;
            border-radius: 10px;
            padding: 14px 16px;
            display: flex;
            gap: 12px;
            align-items: flex-start;
            margin-bottom: 24px;
        ">
            <span style="font-size: 1.15rem; line-height: 1;">💡</span>
            <span style="font-size: 0.8rem; color: #334155; line-height: 1.45;">
                This project is part of the Josh Talks AI – Product Operations Task.
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # If currently inside one of the sub-experiences, show a helpful status indicator
    if current_view == "assignment_results":
        st.markdown(
            """
            <div style="background: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 8px; padding: 10px 12px; margin-bottom: 15px; font-size: 0.8rem; color: #1E40AF; font-weight: 600;">
                Active View: 📊 Assignment Evaluation
            </div>
            """,
            unsafe_allow_html=True
        )
    elif current_view == "try_rating_app":
        st.markdown(
            """
            <div style="background: #FFF7ED; border: 1px solid #FED7AA; border-radius: 8px; padding: 10px 12px; margin-bottom: 15px; font-size: 0.8rem; color: #9A3412; font-weight: 600;">
                Active View: 🧪 Try Rating App (Beta)
            </div>
            """,
            unsafe_allow_html=True
        )

    # Footer at bottom of sidebar
    st.markdown(
        """
        <div style="font-size: 0.76rem; color: #64748B; margin-top: 40px; line-height: 1.5;">
            <div>Built with ❤️ for India</div>
            <div style="color: #94A3B8; font-size: 0.72rem;">Josh Talks AI – Product Operations Task</div>
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
