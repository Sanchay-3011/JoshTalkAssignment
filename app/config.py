"""
Configuration and styling tokens for Josh Talks AI Evaluation Platform.
Provides cached data loaders, custom CSS injection, and design system tokens.
Ensures 100% dark mode immunity and exact visual match to design specification.
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

# Design Tokens
THEME_COLORS = {
    "primary": "#2563EB",
    "navy": "#0F172A",
    "slate": "#64748B",
    "orange": "#EA580C",
    "green": "#16A34A",
    "background": "#F8FAFC",
    "card_bg": "#FFFFFF",
    "border": "#E2E8F0"
}

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

/* Force Light Theme Globally (Complete Dark Mode Immunity) */
:root {
    --primary: #2563EB !important;
    --background: #F8FAFC !important;
    --card-bg: #FFFFFF !important;
    --text-main: #0F172A !important;
    --text-muted: #64748B !important;
    --border: #E2E8F0 !important;
    color-scheme: light !important;
}

html, body, [class*="css"], .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background-color: #F8FAFC !important;
    color: #0F172A !important;
    color-scheme: light !important;
}

/* Comprehensive dark mode suppression */
@media (prefers-color-scheme: dark) {
    :root, html, body, [class*="css"], .stApp, 
    [data-testid="stAppViewContainer"], 
    [data-testid="stHeader"], 
    [data-testid="stSidebar"], 
    [data-testid="stSidebarContent"], 
    section[data-testid="stSidebar"] {
        background-color: #F8FAFC !important;
        color: #0F172A !important;
        color-scheme: light !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"],
    div[data-testid="stVerticalBlockBorderWrapper"] > div {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-color: #E2E8F0 !important;
    }

    p, span, h1, h2, h3, h4, h5, h6, label, div, a {
        color-scheme: light !important;
    }
}

/* Streamlit Header adjustments */
header[data-testid="stHeader"] {
    background-color: #F8FAFC !important;
    height: 1.2rem !important;
}
[data-testid="stDecoration"] {
    display: none !important;
}
#MainMenu {
    visibility: hidden !important;
}

/* Hide auto-generated sidebar multi-page navigation */
[data-testid="stSidebarNav"] {
    display: none !important;
}

/* Sidebar styling */
[data-testid="stSidebar"],
[data-testid="stSidebarContent"],
section[data-testid="stSidebar"] {
    background-color: #F8FAFC !important;
    border-right: 1px solid #E2E8F0 !important;
    color-scheme: light !important;
}

[data-testid="stSidebarContent"] > div:first-child {
    background-color: #F8FAFC !important;
    padding-top: 1.2rem !important;
    padding-left: 1.2rem !important;
    padding-right: 1.2rem !important;
}

/* Main container constraints */
.main .block-container {
    max-width: 1140px !important;
    padding-top: 0.4rem !important;
    padding-bottom: 1.2rem !important;
    background-color: #F8FAFC !important;
}

/* Option Cards - st.container(border=True) */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 16px !important;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04), 0 2px 4px -2px rgba(0, 0, 0, 0.02) !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
}
div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.07), 0 4px 6px -4px rgba(0, 0, 0, 0.04) !important;
}
div[data-testid="stVerticalBlockBorderWrapper"] > div {
    padding: 24px 24px 20px 24px !important;
    background-color: #FFFFFF !important;
    border-radius: 16px !important;
}

/* Sidebar Nav Home Button */
div.st-key-sidebar_nav_home button {
    background: #EFF6FF !important;
    border: 1px solid #DBEAFE !important;
    border-radius: 8px !important;
    padding: 10px 14px !important;
    color: #2563EB !important;
    font-weight: 700 !important;
    font-size: 0.92rem !important;
    box-shadow: none !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    position: relative !important;
    text-align: left !important;
}
div.st-key-sidebar_nav_home button:hover {
    background: #DBEAFE !important;
    border-color: #93C5FD !important;
    color: #1D4ED8 !important;
}
div.st-key-sidebar_nav_home button p {
    color: #2563EB !important;
    font-weight: 700 !important;
    font-size: 0.92rem !important;
    margin: 0 !important;
    display: flex !important;
    align-items: center !important;
    gap: 9px !important;
}
div.st-key-sidebar_nav_home button p::before {
    content: "" !important;
    display: inline-block !important;
    width: 17px !important;
    height: 17px !important;
    background-color: #2563EB !important;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%232563EB'%3E%3Cpath d='M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z'/%3E%3C/svg%3E") no-repeat center / contain !important;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%232563EB'%3E%3Cpath d='M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z'/%3E%3C/svg%3E") no-repeat center / contain !important;
}
div.st-key-sidebar_nav_home button::after {
    content: "›" !important;
    font-size: 1.35rem !important;
    font-weight: 600 !important;
    color: #2563EB !important;
    margin-left: auto !important;
    line-height: 1 !important;
}

/* Primary Action Buttons */
div.st-key-btn_view_results button {
    background-color: #1D4ED8 !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 12px 20px !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    box-shadow: 0 1px 2px rgba(29, 78, 216, 0.2) !important;
    transition: all 0.15s ease !important;
    width: 100% !important;
}
div.st-key-btn_view_results button:hover {
    background-color: #1E40AF !important;
    color: #FFFFFF !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 6px -1px rgba(29, 78, 216, 0.3) !important;
}
div.st-key-btn_view_results button p {
    color: #FFFFFF !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    margin: 0 !important;
}

div.st-key-btn_try_rating button {
    background-color: #EA580C !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 12px 20px !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    box-shadow: 0 1px 2px rgba(234, 88, 12, 0.2) !important;
    transition: all 0.15s ease !important;
    width: 100% !important;
}
div.st-key-btn_try_rating button:hover {
    background-color: #C2410C !important;
    color: #FFFFFF !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 6px -1px rgba(234, 88, 12, 0.3) !important;
}
div.st-key-btn_try_rating button p {
    color: #FFFFFF !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    margin: 0 !important;
}

/* Metric card container for results view */
.jt-kpi-card {
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 12px !important;
    padding: 18px 20px !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
}
.jt-kpi-card:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08) !important;
}
.jt-kpi-title {
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    color: #64748B !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
    margin-bottom: 4px !important;
}
.jt-kpi-value {
    font-size: 1.85rem !important;
    font-weight: 800 !important;
    color: #0F172A !important;
    line-height: 1.2 !important;
}
.jt-kpi-sub {
    font-size: 0.75rem !important;
    color: #94A3B8 !important;
    margin-top: 4px !important;
}

/* Badges */
.jt-badge {
    display: inline-block !important;
    padding: 3px 10px !important;
    border-radius: 9999px !important;
    font-size: 0.75rem !important;
    font-weight: 600 !important;
}
.jt-badge-gold {
    background: #FEF3C7 !important;
    color: #92400E !important;
    border: 1px solid #FDE68A !important;
}
.jt-badge-blue {
    background: #DBEAFE !important;
    color: #1E40AF !important;
    border: 1px solid #BFDBFE !important;
}
.jt-badge-slate {
    background: #F1F5F9 !important;
    color: #475569 !important;
    border: 1px solid #E2E8F0 !important;
}

/* Clean tables */
table {
    border-collapse: separate !important;
    border-spacing: 0 !important;
    width: 100% !important;
    border-radius: 8px !important;
    overflow: hidden !important;
    border: 1px solid #E2E8F0 !important;
    background-color: #FFFFFF !important;
}
th {
    background-color: #F8FAFC !important;
    color: #475569 !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.04em !important;
    padding: 12px 16px !important;
}
td {
    padding: 12px 16px !important;
    font-size: 0.9rem !important;
    border-bottom: 1px solid #F1F5F9 !important;
    background-color: #FFFFFF !important;
    color: #0F172A !important;
}

/* Force light inputs */
input, textarea, select, [data-baseweb="input"], [data-baseweb="select"] {
    background-color: #FFFFFF !important;
    color: #0F172A !important;
    border-color: #CBD5E1 !important;
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
