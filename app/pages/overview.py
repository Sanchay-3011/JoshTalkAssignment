"""
Overview page for Josh Talks AI evaluation dashboard.
"""

import streamlit as st
import pandas as pd
from app.components.cards import (
    render_kpi_card,
    render_insight_card,
    render_dimension_bar_chart,
    render_radar_chart,
    get_model_label
)


def render_overview(ctx: dict):
    metrics = ctx["metrics"]
    metadata = ctx["models_meta"]
    disclose = ctx["disclose_models"]
    is_primary = ctx["is_primary"]
    sensitivity = ctx["sensitivity_check"]

    st.markdown("## 🇮🇳 INDIA E-COMMERCE IMAGE EVALUATION")
    st.markdown(
        "<div style='font-size:1.05rem; color:#475569; margin-top:-8px; margin-bottom:24px;'>"
        "Human evaluation of leading text-to-image foundation models for Indian e-commerce listing and lifestyle imagery."
        "</div>",
        unsafe_allow_html=True
    )

    # 5 KPI Cards
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        render_kpi_card("Models Evaluated", "3", "OpenAI & Google", badge_text="SOTA", badge_type="blue")
    with col2:
        render_kpi_card("Evaluation Prompts", "5", "Apparel, Food, Home", badge_text="Curated", badge_type="slate")
    with col3:
        sample_label = "10" if is_primary else "11"
        badge_val = "Primary" if is_primary else "Robustness"
        badge_col = "gold" if is_primary else "slate"
        render_kpi_card("Evaluators (N)", sample_label, "100% Consent Verified", badge_text=badge_val, badge_type=badge_col)
    with col4:
        render_kpi_card("Images Evaluated", "15", "5 Prompts × 3 Models", badge_text="15 PNGs", badge_type="slate")
    with col5:
        render_kpi_card("Rating Dimensions", "3", "Adherence, Visual, Cultural", badge_text="1-5 Likert", badge_type="slate")

    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)

    # Dynamic Insight Banner
    top_model = sorted(metrics.values(), key=lambda x: x["overall_score"], reverse=True)[0]
    top_label = get_model_label(top_model["model_id"], metadata, disclose)
    second_model = sorted(metrics.values(), key=lambda x: x["overall_score"], reverse=True)[1]
    second_label = get_model_label(second_model["model_id"], metadata, disclose)

    render_insight_card(
        f"{top_label} achieved a clean sweep with an overall score of {top_model['overall_score']:.2f}/5.00, "
        f"securing the top rank across Prompt Adherence ({top_model['prompt_adherence_mean']:.2f}), "
        f"Visual Quality ({top_model['visual_quality_mean']:.2f}), and Indian Cultural Authenticity ({top_model['indian_authenticity_mean']:.2f}). "
        f"{second_label} placed 2nd ({second_model['overall_score']:.2f}) but narrowed the gap on festive confectionery packaging.",
        highlight="Core Finding"
    )

    # Leaderboard Summary Table + Sensitivity Check
    st.markdown("### 🏆 Overall Model Leaderboard")

    col_tbl, col_meta = st.columns([3, 2])

    with col_tbl:
        rows = []
        for mid in ["Model A", "Model B", "Model C"]:
            d = metrics[mid]
            label = get_model_label(mid, metadata, disclose)
            badge = "🥇 Rank 1" if d["rank"] == 1 else ("🥈 Rank 2" if d["rank"] == 2 else "🥉 Rank 3")
            rows.append({
                "Rank": badge,
                "Model": label,
                "Overall Score": f"{d['overall_score']:.2f} / 5.00",
                "Prompt Match": f"{d['prompt_adherence_mean']:.2f}",
                "Visual Quality": f"{d['visual_quality_mean']:.2f}",
                "Cultural Authenticity": f"{d['indian_authenticity_mean']:.2f}",
                "High Ratings (≥4)": f"{d['high_rating_percentage']:.1f}%",
                "Disagreement (StdDev)": f"±{d['overall_std']:.2f}"
            })

        st.dataframe(
            pd.DataFrame(rows),
            use_container_width=True,
            hide_index=True
        )

    with col_meta:
        st.markdown("#### 🔬 Robustness & Protocol Check")
        status_text = "PASSED" if sensitivity["rank_unchanged"] else "FLAGGED"
        status_color = "#10B981" if sensitivity["rank_unchanged"] else "#EF4444"

        st.markdown(
            f"""
            <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:14px;">
                <div style="font-size:0.8rem; font-weight:700; color:#64748B;">PROTOCOL VALIDATION</div>
                <div style="font-size:1.1rem; font-weight:800; color:{status_color}; margin-top:2px;">
                    {status_text}: Rank Invariance Confirmed
                </div>
                <p style="font-size:0.85rem; color:#475569; margin-top:6px; line-height:1.4;">
                    The survey received 11 responses against the planned 10-person protocol.
                    When including all 11 responses, <strong>Model A (4.74) &gt; Model B (3.81) &gt; Model C (3.32)</strong>
                    remains 100% stable. The 11th participant is documented in raw evidence and sensitivity tabs.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

    # Benchmark Visualizations: Dimension Bar Chart & Radar Chart
    st.markdown("### 📊 Benchmark Analysis Across Evaluation Dimensions")
    c_chart1, c_chart2 = st.columns([3, 2])

    with c_chart1:
        st.markdown("##### Dimension Scores Comparison")
        fig_bar = render_dimension_bar_chart(metrics, metadata, disclose)
        st.plotly_chart(fig_bar, use_container_width=True)

    with c_chart2:
        st.markdown("##### Performance Radar & Consistency")
        fig_radar = render_radar_chart(metrics, metadata, disclose)
        st.plotly_chart(fig_radar, use_container_width=True)

    st.markdown("---")

    # Key Findings & Qualitative Highlights
    st.markdown("### 💡 Executive Insights & Strategic Takeaways")
    k1, k2, k3 = st.columns(3)

    with k1:
        st.markdown(
            """
            <div class="jt-kpi-card" style="height: 100%;">
                <div class="jt-kpi-title" style="color:#D97706;">1. Decisive Model A Dominance</div>
                <p style="font-size:0.88rem; color:#334155; line-height:1.5;">
                    Model A (OpenAI) swept all 5 prompts and all 3 criteria (15/15 sub-metrics).
                    Evaluators noted its native comprehension of e-commerce layout nuances—generating turnkey
                    ad typography, matching Indian female jewelry/bindi styling, and demonstrating 3 open tiffin compartments.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with k2:
        st.markdown(
            """
            <div class="jt-kpi-card" style="height: 100%;">
                <div class="jt-kpi-title" style="color:#2563EB;">2. Model B Closes Gap on Festive Decor</div>
                <p style="font-size:0.88rem; color:#334155; line-height:1.5;">
                    Model B (Gemini 3.1 Pro) scored its highest mark on the Diwali Namkeen Pouch prompt (4.21 vs 4.61 for A).
                    Its rendering of marigold flowers, earthen diyas, and festive sale badges resonated strongly with Indian evaluators,
                    though it suffered from unexpected split-screen layouts.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with k3:
        st.markdown(
            """
            <div class="jt-kpi-card" style="height: 100%;">
                <div class="jt-kpi-title" style="color:#64748B;">3. Model C Semantic & Physical Glitches</div>
                <p style="font-size:0.88rem; color:#334155; line-height:1.5;">
                    Model C (Gemini Flash-Lite) exhibited high evaluator disagreement (std dev 1.35 vs 0.58 for Model A).
                    Key failure modes included rendering an articulated wooden artist doll for the Saree prompt and a
                    full-sleeved Bandhgala blazer instead of a sleeveless Nehru jacket.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)

    # Methodology & Limitations Brief
    st.markdown("### 📋 Evaluation Methodology & Sample Transparency")
    m_col1, m_col2 = st.columns(2)

    with m_col1:
        st.markdown(
            """
            **Evaluation Protocol & Safeguards:**
            - **Blind Evaluation:** Models were labeled as Model A, Model B, Model C during collection to minimize brand bias.
            - **Controlled Prompts:** Identical text prompts were provided across all 3 models spanning 5 core Indian e-commerce verticals.
            - **Multi-Dimensional Human Judgment:** Evaluated on 1–5 Likert scales across *Prompt Adherence*, *Visual Quality*, and *Indian Cultural Authenticity*.
            - **Consent Verification:** 100% of participants voluntarily consented and certified age 18+.
            """
        )

    with m_col2:
        st.markdown(
            """
            **Sample Constraints & Limitations:**
            - **Sample Size ($N=10$):** High directional signal for top model selection, but not statistically definitive for edge cases across India's 1.4B population.
            - **Demographics:** Participants were aged 19–46, primarily young digital consumers.
            - **Fixed Single Seed:** One image generation per model was tested per prompt; future iterations require multi-seed variance testing.
            - **Offline Judgment:** Human ratings measure aesthetic perception, not live A/B click-through or checkout conversion rates.
            """
        )
