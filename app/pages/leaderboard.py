"""
Interactive Model Leaderboard page for Josh Talks AI evaluation.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app.components.cards import (
    render_kpi_card,
    get_model_label,
    render_radar_chart
)


def render_leaderboard(ctx: dict):
    metrics = ctx["metrics"]
    metadata = ctx["models_meta"]
    disclose = ctx["disclose_models"]
    prompt_metrics = ctx["prompt_metrics"]
    stats_meta = ctx["stats_meta"]
    is_primary = ctx["is_primary"]

    st.markdown("## 🏆 MODEL BENCHMARK LEADERBOARD")
    st.markdown(
        "<div style='font-size:1.0rem; color:#475569; margin-top:-8px; margin-bottom:20px;'>"
        "Comprehensive model rankings based on 150 primary human ratings across prompt match, visual fidelity, and cultural authenticity."
        "</div>",
        unsafe_allow_html=True
    )

    # Top Controls: Sort Order & Dimension Filter
    f_col1, f_col2, f_col3 = st.columns([2, 2, 2])
    with f_col1:
        sort_dimension = st.selectbox(
            "Sort Leaderboard By:",
            ["Overall Score", "Prompt Adherence", "Visual Quality", "Indian Authenticity", "High Rating %", "Consistency Index"]
        )
    with f_col2:
        model_inspect = st.selectbox(
            "Select Model for Deep Dive:",
            ["Model A", "Model B", "Model C"],
            index=0
        )
    with f_col3:
        st.markdown(
            f"<div style='padding-top:28px; font-size:0.85rem; color:#64748B;'>"
            f"Cohort: <strong>{'Primary (N=10)' if is_primary else 'Sensitivity (N=11)'}</strong>"
            f"</div>",
            unsafe_allow_html=True
        )

    # Sort mapping
    sort_key_map = {
        "Overall Score": "overall_score",
        "Prompt Adherence": "prompt_adherence_mean",
        "Visual Quality": "visual_quality_mean",
        "Indian Authenticity": "indian_authenticity_mean",
        "High Rating %": "high_rating_percentage",
        "Consistency Index": "consistency_index"
    }
    target_key = sort_key_map[sort_dimension]

    # Build leaderboard data
    model_rows = []
    for mid, d in metrics.items():
        label = get_model_label(mid, metadata, disclose)
        rank_badge = "🥇 1st" if d["rank"] == 1 else ("🥈 2nd" if d["rank"] == 2 else "🥉 3rd")
        model_rows.append({
            "Rank": rank_badge,
            "Model Identifier": mid,
            "Model Name": label,
            "Overall Score": d["overall_score"],
            "Prompt Adherence": d["prompt_adherence_mean"],
            "Visual Quality": d["visual_quality_mean"],
            "Indian Authenticity": d["indian_authenticity_mean"],
            "High Rating % (≥4)": f"{d['high_rating_percentage']:.1f}%",
            "Consistency Index": f"{d['consistency_index']:.3f}",
            "Std Deviation (Disagreement)": f"±{d['overall_std']:.2f}",
            "_sort_val": d[target_key]
        })

    df_lb = pd.DataFrame(model_rows).sort_values(by="_sort_val", ascending=False).drop(columns=["_sort_val"])

    # Display clean table
    st.dataframe(
        df_lb,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # Detailed Model Inspector Deep Dive
    st.markdown(f"### 🔍 Model Deep Dive: {get_model_label(model_inspect, metadata, disclose)}")

    m_spec = metadata.get(model_inspect, {})
    m_metric = metrics.get(model_inspect, {})
    ci_data = stats_meta.get("variance_and_confidence_intervals_primary", {}).get(model_inspect, {})

    col_meta1, col_meta2, col_meta3, col_meta4 = st.columns(4)
    with col_meta1:
        render_kpi_card("Overall Mean", f"{m_metric['overall_score']:.2f} / 5", f"Median: {m_metric['overall_median']:.2f}")
    with col_meta2:
        render_kpi_card("95% Confidence Interval", f"[{ci_data.get('ci_95', [0,0])[0]:.2f}, {ci_data.get('ci_95', [0,0])[1]:.2f}]", f"SE: ±{ci_data.get('standard_error', 0):.2f}")
    with col_meta3:
        render_kpi_card("High Rating %", f"{m_metric['high_rating_percentage']:.1f}%", f"Ratings ≥ 4.0")
    with col_meta4:
        render_kpi_card("Rater Disagreement (σ)", f"±{m_metric['overall_std']:.2f}", f"Consistency: {m_metric['consistency_index']:.3f}")

    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

    c_info1, c_info2 = st.columns([1, 1])
    with c_info1:
        st.markdown(
            f"""
            <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:16px;">
                <h5 style="margin-top:0; color:#1E293B;">Technical & Generation Specifications</h5>
                <ul style="font-size:0.88rem; color:#475569; line-height:1.7; padding-left:20px;">
                    <li><strong>Provider:</strong> {m_spec.get('company', 'Unknown')}</li>
                    <li><strong>Exact Foundation Model:</strong> {m_spec.get('model_name', 'Unknown')}</li>
                    <li><strong>Resolution / Generation Size:</strong> {m_spec.get('resolution', 'N/A')}</li>
                    <li><strong>Aspect Ratio Behavior:</strong> {m_spec.get('aspect_ratio_behavior', 'N/A')}</li>
                    <li><strong>API Documentation:</strong> <a href="{m_spec.get('documentation_url', '#')}" target="_blank">Official Docs</a></li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c_info2:
        st.markdown(
            f"""
            <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:16px;">
                <h5 style="margin-top:0; color:#1E293B;">Evaluator Qualitative Profile</h5>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:8px;">
                    <strong>Observed Strengths:</strong><br>{m_spec.get('strengths', 'None documented.')}
                </p>
                <p style="font-size:0.85rem; color:#334155;">
                    <strong>Observed Weaknesses / Edge Cases:</strong><br>{m_spec.get('weaknesses', 'None documented.')}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)

    # Prompt Breakdown for this specific model
    st.markdown(f"#### 📊 Prompt-by-Prompt Performance for {model_inspect}")

    p_names = []
    pa_list = []
    vq_list = []
    ia_list = []
    ov_list = []

    for pid, p_data in prompt_metrics.items():
        p_names.append(p_data["prompt_name"])
        m_perf = p_data["models"][model_inspect]
        pa_list.append(m_perf["prompt_adherence"])
        vq_list.append(m_perf["visual_quality"])
        ia_list.append(m_perf["indian_authenticity"])
        ov_list.append(m_perf["overall"])

    fig_prompt_model = go.Figure()
    fig_prompt_model.add_trace(go.Bar(name="Prompt Adherence", x=p_names, y=pa_list, marker_color="#3B82F6"))
    fig_prompt_model.add_trace(go.Bar(name="Visual Quality", x=p_names, y=vq_list, marker_color="#10B981"))
    fig_prompt_model.add_trace(go.Bar(name="Indian Authenticity", x=p_names, y=ia_list, marker_color="#F59E0B"))
    fig_prompt_model.add_trace(go.Scatter(name="Overall Mean", x=p_names, y=ov_list, mode="lines+markers", line=dict(color="#1E293B", width=3)))

    fig_prompt_model.update_layout(
        barmode="group",
        yaxis=dict(range=[0, 5.5], title="Score (1-5)", gridcolor="#F1F5F9"),
        xaxis=dict(tickangle=-10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=30, b=50),
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        height=360,
        font=dict(family="Plus Jakarta Sans", color="#1E293B")
    )
    st.plotly_chart(fig_prompt_model, use_container_width=True)
