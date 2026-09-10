"""
UI Components and Plotly visualizers for Josh Talks AI Evaluation Platform.
Implements executive KPI cards, radar comparison charts, score distributions, and heatmaps.
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np


def render_kpi_card(title: str, value: str, subtitle: str = "", badge_text: str = None, badge_type: str = "slate"):
    badge_html = f'<span class="jt-badge jt-badge-{badge_type}" style="float: right;">{badge_text}</span>' if badge_text else ""
    html = f"""
    <div class="jt-kpi-card">
        {badge_html}
        <div class="jt-kpi-title">{title}</div>
        <div class="jt-kpi-value">{value}</div>
        <div class="jt-kpi-sub">{subtitle}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def render_insight_card(text: str, highlight: str = ""):
    hl_prefix = f"<strong>{highlight}</strong> — " if highlight else ""
    html = f"""
    <div class="jt-insight-box">
        {hl_prefix}{text}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def get_model_label(model_key: str, metadata: dict, disclose: bool = False) -> str:
    if not disclose or model_key not in metadata:
        return model_key
    m = metadata[model_key]
    return f"{model_key} ({m['company']} — {m['model_name']})"


def render_dimension_bar_chart(metrics: dict, metadata: dict, disclose: bool = False):
    categories = ["Prompt Adherence", "Visual Quality", "Indian Authenticity", "Overall Score"]

    fig = go.Figure()
    colors = {
        "Model A": "#F59E0B",   # Warm Amber / Gold (Winner)
        "Model B": "#3B82F6",   # Royal Blue
        "Model C": "#94A3B8"    # Cool Slate
    }

    for mid, data in metrics.items():
        label = get_model_label(mid, metadata, disclose)
        values = [
            data["prompt_adherence_mean"],
            data["visual_quality_mean"],
            data["indian_authenticity_mean"],
            data["overall_score"]
        ]
        fig.add_trace(go.Bar(
            name=label,
            x=categories,
            y=values,
            text=[f"{v:.2f}" for v in values],
            textposition="outside",
            marker_color=colors.get(mid, "#64748B"),
            marker_line_width=0
        ))

    fig.update_layout(
        barmode="group",
        yaxis=dict(range=[0, 5.5], title="Rating (1-5 Likert Scale)", gridcolor="#F1F5F9"),
        xaxis=dict(title="", tickfont=dict(size=12, family="Plus Jakarta Sans")),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=30, b=20),
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        height=380,
        font=dict(family="Plus Jakarta Sans", color="#1E293B")
    )
    return fig


def render_radar_chart(metrics: dict, metadata: dict, disclose: bool = False):
    dimensions = ["Prompt Adherence", "Visual Quality", "Indian Authenticity", "High Rating % (Normalized)", "Consistency"]

    fig = go.Figure()
    colors = {
        "Model A": "rgba(245, 158, 11, 0.4)",
        "Model B": "rgba(59, 130, 246, 0.35)",
        "Model C": "rgba(148, 163, 184, 0.3)"
    }
    line_colors = {
        "Model A": "#D97706",
        "Model B": "#2563EB",
        "Model C": "#64748B"
    }

    for mid, d in metrics.items():
        label = get_model_label(mid, metadata, disclose)
        # normalize high rating % to 0-5 scale for radar parity
        high_norm = (d["high_rating_percentage"] / 100.0) * 5.0
        # normalize consistency index (0.5 to 1.0) to 1-5 scale
        consist_norm = d["consistency_index"] * 5.0

        r_values = [
            d["prompt_adherence_mean"],
            d["visual_quality_mean"],
            d["indian_authenticity_mean"],
            high_norm,
            consist_norm
        ]
        # Close the loop
        r_values.append(r_values[0])
        theta_closed = dimensions + [dimensions[0]]

        fig.add_trace(go.Scatterpolar(
            r=r_values,
            theta=theta_closed,
            fill="toself",
            name=label,
            fillcolor=colors.get(mid, "rgba(100,100,100,0.2)"),
            line=dict(color=line_colors.get(mid, "#475569"), width=2)
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 5], gridcolor="#E2E8F0"),
            angularaxis=dict(gridcolor="#E2E8F0", tickfont=dict(size=11, family="Plus Jakarta Sans"))
        ),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        margin=dict(l=40, r=40, t=20, b=40),
        paper_bgcolor="#FFFFFF",
        height=380,
        font=dict(family="Plus Jakarta Sans", color="#1E293B")
    )
    return fig


def render_prompt_breakdown_chart(prompt_metrics: dict, metadata: dict, disclose: bool = False):
    prompt_names = [p["prompt_name"] for p in prompt_metrics.values()]

    fig = go.Figure()
    colors = {"Model A": "#F59E0B", "Model B": "#3B82F6", "Model C": "#94A3B8"}

    for mid in ["Model A", "Model B", "Model C"]:
        label = get_model_label(mid, metadata, disclose)
        scores = [p["models"][mid]["overall"] for p in prompt_metrics.values()]
        fig.add_trace(go.Bar(
            name=label,
            x=prompt_names,
            y=scores,
            text=[f"{s:.2f}" for s in scores],
            textposition="outside",
            marker_color=colors[mid]
        ))

    fig.update_layout(
        barmode="group",
        yaxis=dict(range=[0, 5.5], title="Overall Score (1-5)", gridcolor="#F1F5F9"),
        xaxis=dict(tickangle=-15, tickfont=dict(size=11)),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=30, b=70),
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        height=380,
        font=dict(family="Plus Jakarta Sans", color="#1E293B")
    )
    return fig


def render_rater_disagreement_heatmap(df_primary: pd.DataFrame):
    """Generates standard deviation of ratings by Prompt x Model matrix."""
    grouped = df_primary.groupby(["prompt_name", "model_id"])["overall_score"].std().unstack()

    fig = px.imshow(
        grouped,
        labels=dict(x="Model", y="Prompt", color="Std Deviation (Disagreement)"),
        x=grouped.columns,
        y=grouped.index,
        color_continuous_scale="Blues",
        text_auto=".2f"
    )
    fig.update_layout(
        margin=dict(l=20, r=20, t=30, b=20),
        height=340,
        font=dict(family="Plus Jakarta Sans", color="#1E293B")
    )
    return fig
