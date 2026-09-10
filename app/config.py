"""
Configuration and styling tokens for Josh Talks AI Evaluation Platform.
Provides cached data loaders, custom CSS injection, and design system tokens.
"""

import json
import os
import streamlit as st
import pandas as pd
from PIL import Image

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
METADATA_DIR = os.path.join(DATA_DIR, "metadata")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")

# Design Tokens (Deep navy / Slate / Gold accent)
THEME_COLORS = {
    "primary": "#1E3A8A",      # Royal Navy
    "secondary": "#3B82F6",    # Vivid Blue
    "accent": "#F59E0B",       # Warm Gold / Amber
    "success": "#10B981",      # Emerald Green
    "warning": "#F97316",      # Bright Orange
    "danger": "#EF4444",       # Rose Red
    "background_card": "#FFFFFF",
    "border": "#E2E8F0",
    "text_dark": "#0F172A",
    "text_muted": "#64748B"
}

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Hide default streamlit header decoration */
header[data-testid="stHeader"] {
    background: transparent;
}

/* Metric card container */
.jt-kpi-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 18px 20px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.jt-kpi-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
}
.jt-kpi-title {
    font-size: 0.78rem;
    font-weight: 600;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 4px;
}
.jt-kpi-value {
    font-size: 1.85rem;
    font-weight: 800;
    color: #0F172A;
    line-height: 1.2;
}
.jt-kpi-sub {
    font-size: 0.75rem;
    color: #94A3B8;
    margin-top: 4px;
}

/* Badges */
.jt-badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 600;
}
.jt-badge-gold {
    background: #FEF3C7;
    color: #92400E;
    border: 1px solid #FDE68A;
}
.jt-badge-blue {
    background: #DBEAFE;
    color: #1E40AF;
    border: 1px solid #BFDBFE;
}
.jt-badge-slate {
    background: #F1F5F9;
    color: #475569;
    border: 1px solid #E2E8F0;
}

/* Insight card */
.jt-insight-box {
    background: #F8FAFC;
    border-left: 4px solid #3B82F6;
    border-radius: 0 8px 8px 0;
    padding: 14px 18px;
    margin: 12px 0;
    color: #1E293B;
    font-size: 0.92rem;
    line-height: 1.5;
}

/* Leaderboard row styling */
.jt-rank-1 {
    background: linear-gradient(90deg, rgba(254,243,199,0.3) 0%, rgba(255,255,255,0) 100%);
    border-left: 4px solid #F59E0B;
}

/* Clean tables */
table {
    border-collapse: separate;
    border-spacing: 0;
    width: 100%;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid #E2E8F0;
}
th {
    background-color: #F8FAFC !important;
    color: #475569 !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    padding: 12px 16px !important;
}
td {
    padding: 12px 16px !important;
    font-size: 0.9rem !important;
    border-bottom: 1px solid #F1F5F9;
}
</style>
"""


def apply_custom_css():
    """Inject polished stylesheet into Streamlit."""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


@st.cache_data
def load_evaluations() -> pd.DataFrame:
    path = os.path.join(PROCESSED_DIR, "evaluations_normalized.csv")
    return pd.read_csv(path)


@st.cache_data
def load_participants() -> pd.DataFrame:
    path = os.path.join(PROCESSED_DIR, "participants_anonymized.csv")
    return pd.read_csv(path)


@st.cache_data
def load_models_metadata() -> dict:
    path = os.path.join(METADATA_DIR, "models.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@st.cache_data
def load_prompts_metadata() -> dict:
    path = os.path.join(METADATA_DIR, "prompts.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@st.cache_data
def load_qualitative_notes() -> dict:
    path = os.path.join(METADATA_DIR, "qualitative_notes.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@st.cache_data
def load_model_metrics_primary() -> dict:
    path = os.path.join(PROCESSED_DIR, "model_metrics_primary.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@st.cache_data
def load_model_metrics_robustness() -> dict:
    path = os.path.join(PROCESSED_DIR, "model_metrics_robustness.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@st.cache_data
def load_prompt_metrics() -> dict:
    path = os.path.join(PROCESSED_DIR, "prompt_metrics.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@st.cache_data
def load_sensitivity_check() -> dict:
    path = os.path.join(PROCESSED_DIR, "sensitivity_check.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@st.cache_data
def load_statistical_analysis() -> dict:
    path = os.path.join(PROCESSED_DIR, "statistical_analysis.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_image(rel_path: str):
    """Load image safely from relative path."""
    full_path = os.path.join(BASE_DIR, rel_path)
    if os.path.exists(full_path):
        return Image.open(full_path)
    return None
