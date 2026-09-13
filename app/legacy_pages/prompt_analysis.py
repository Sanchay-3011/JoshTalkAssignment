"""
Prompt Analysis page for Josh Talks AI evaluation.
Displays side-by-side model outputs, rating distributions, and evidence-grounded critique.
"""

import streamlit as st
import plotly.graph_objects as go
from app.config import get_image
from app.components.cards import get_model_label, render_kpi_card


def render_prompt_analysis(ctx: dict):
    prompts_meta = ctx["prompts_meta"]
    qualitative_notes = ctx["qualitative_notes"]
    prompt_metrics = ctx["prompt_metrics"]
    models_meta = ctx["models_meta"]
    disclose = ctx["disclose_models"]

    st.markdown("## 🔍 PROMPT-LEVEL EVALUATION ANALYSIS")
    st.markdown(
        "<div style='font-size:1.0rem; color:#475569; margin-top:-8px; margin-bottom:20px;'>"
        "Inspect how each foundation model interpreted specific Indian cultural, apparel, and commercial e-commerce prompts."
        "</div>",
        unsafe_allow_html=True
    )

    # Prompt Selector
    prompt_options = {
        "P1": "Prompt 1: Red Banarasi Silk Saree (Apparel)",
        "P2": "Prompt 2: Stainless Steel Indian Tiffin Box (Kitchenware)",
        "P3": "Prompt 3: Festive Namkeen Snack Pouch (FMCG / Diwali)",
        "P4": "Prompt 4: Beige Cotton Kurta Set (Catalog Wear)",
        "P5": "Prompt 5: Navy Blue Nehru Jacket (Men's Festive)"
    }

    selected_pid = st.selectbox(
        "Choose an Evaluation Prompt:",
        list(prompt_options.keys()),
        format_func=lambda k: prompt_options[k]
    )

    p_info = prompts_meta[selected_pid]
    p_notes = qualitative_notes.get(selected_pid, {})
    p_scores = prompt_metrics.get(selected_pid, {}).get("models", {})

    # Display Prompt Context Card
    st.markdown(
        f"""
        <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:18px; margin-bottom:20px;">
            <div style="font-size:0.75rem; font-weight:700; color:#3B82F6; text-transform:uppercase; letter-spacing:0.05em;">
                E-COMMERCE USE CASE & SPECIFICATION · {p_info['category']}
            </div>
            <div style="font-size:1.05rem; font-weight:700; color:#0F172A; margin-top:4px;">
                "{p_info['prompt_text']}"
            </div>
            <div style="font-size:0.85rem; color:#64748B; margin-top:8px;">
                <strong>Catalog Intent:</strong> {p_info['use_case']} · <strong>Cultural Nuance:</strong> {p_info['cultural_nuance']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Side-by-Side Model Images (3 Columns)
    st.markdown("### 🖼️ Generated Outputs & Performance Scores")
    colA, colB, colC = st.columns(3)

    models_order = [("Model A", colA), ("Model B", colB), ("Model C", colC)]

    for mid, col in models_order:
        with col:
            m_label = get_model_label(mid, models_meta, disclose)
            img_rel_path = p_info["images"][mid]
            img = get_image(img_rel_path)

            score_data = p_scores.get(mid, {})
            ov = score_data.get("overall", 0.0)
            pa = score_data.get("prompt_adherence", 0.0)
            vq = score_data.get("visual_quality", 0.0)
            ia = score_data.get("indian_authenticity", 0.0)

            badge_color = "gold" if mid == "Model A" else ("blue" if mid == "Model B" else "slate")
            st.markdown(f"#### {mid}")
            st.markdown(f"<span class='jt-badge jt-badge-{badge_color}'>{m_label}</span>", unsafe_allow_html=True)

            if img:
                st.image(img, use_container_width=True)
            else:
                st.warning(f"Image not found at {img_rel_path}")

            # Mini Score Metrics
            st.markdown(
                f"""
                <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:12px; margin-top:10px;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                        <span style="font-size:0.85rem; font-weight:700; color:#0F172A;">Overall Score</span>
                        <span style="font-size:0.95rem; font-weight:800; color:#1E3A8A;">{ov:.2f} / 5</span>
                    </div>
                    <div style="font-size:0.8rem; color:#475569; line-height:1.5;">
                        • Prompt Adherence: <strong>{pa:.2f}</strong><br>
                        • Visual Quality: <strong>{vq:.2f}</strong><br>
                        • Indian Authenticity: <strong>{ia:.2f}</strong><br>
                        • Disagreement (σ): <strong>±{score_data.get('overall_std', 0):.2f}</strong>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)

    # Qualitative Observations & Evidence Grounding
    st.markdown("### 📝 Observed Qualitative Strengths & Failure Modes")
    obs = p_notes.get("observations", {})

    q_col1, q_col2, q_col3 = st.columns(3)
    for mid, q_col in [("Model A", q_col1), ("Model B", q_col2), ("Model C", q_col3)]:
        with q_col:
            m_obs = obs.get(mid, {})
            st.markdown(f"##### {mid} Visual Audit")
            st.markdown(
                f"""
                <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:14px; min-height:220px;">
                    <div style="font-size:0.8rem; font-weight:700; color:#10B981;">✓ OBSERVED STRENGTHS</div>
                    <p style="font-size:0.83rem; color:#334155; margin-top:4px; margin-bottom:12px;">
                        {m_obs.get('visual_strengths', 'N/A')}
                    </p>
                    <div style="font-size:0.8rem; font-weight:700; color:#EF4444;">✗ OBSERVED DEFECTS / LIMITATIONS</div>
                    <p style="font-size:0.83rem; color:#334155; margin-top:4px; margin-bottom:8px;">
                        {m_obs.get('visual_weaknesses', 'N/A')}
                    </p>
                    <div style="font-size:0.75rem; color:#64748B;">
                        <strong>Aspect Ratio / Format:</strong> {m_obs.get('aspect_ratio', 'N/A')}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

    # Evaluation Takeaway Banner
    takeaway = p_notes.get("takeaway", "")
    if takeaway:
        st.markdown(
            f"""
            <div style="background:#EFF6FF; border-left:4px solid #2563EB; border-radius:0 8px 8px 0; padding:14px 18px;">
                <span style="font-size:0.85rem; font-weight:700; color:#1E40AF;">EVALUATION TAKEAWAY:</span>
                <span style="font-size:0.88rem; color:#1E293B; margin-left:6px;">{takeaway}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Score Distribution Histogram across the 3 models for this prompt
    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
    st.markdown("#### 📊 Rating Distribution for this Prompt (1 to 5 Stars)")

    dist_fig = go.Figure()
    colors = {"Model A": "#F59E0B", "Model B": "#3B82F6", "Model C": "#94A3B8"}

    for mid in ["Model A", "Model B", "Model C"]:
        dist = p_scores.get(mid, {}).get("score_distribution", {})
        x_vals = [f"{s} Star" for s in range(1, 6)]
        y_vals = [dist.get(str(s), 0) for s in range(1, 6)]

        dist_fig.add_trace(go.Bar(
            name=mid,
            x=x_vals,
            y=y_vals,
            marker_color=colors[mid]
        ))

    dist_fig.update_layout(
        barmode="group",
        yaxis=dict(title="Number of Evaluators", gridcolor="#F1F5F9"),
        xaxis=dict(title="Score"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=30, b=20),
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        height=300,
        font=dict(family="Plus Jakarta Sans", color="#1E293B")
    )
    st.plotly_chart(dist_fig, use_container_width=True)
