"""
Side-by-side Image Comparison page for Josh Talks AI evaluation.
High-resolution visual inspection tool comparing model generations side-by-side.
"""

import streamlit as st
from app.config import get_image
from app.components.cards import get_model_label


def render_image_comparison(ctx: dict):
    prompts_meta = ctx["prompts_meta"]
    models_meta = ctx["models_meta"]
    prompt_metrics = ctx["prompt_metrics"]
    qualitative_notes = ctx["qualitative_notes"]
    disclose = ctx["disclose_models"]

    st.markdown("## 🔍 SIDE-BY-SIDE IMAGE INSPECTOR")
    st.markdown(
        "<div style='font-size:1.0rem; color:#475569; margin-top:-8px; margin-bottom:20px;'>"
        "High-resolution visual inspection tool designed for AI evaluation engineers and catalog creative directors."
        "</div>",
        unsafe_allow_html=True
    )

    c_sel1, c_sel2 = st.columns([2, 2])
    with c_sel1:
        p_keys = list(prompts_meta.keys())
        selected_pid = st.selectbox(
            "Select Evaluation Prompt:",
            p_keys,
            format_func=lambda k: f"{prompts_meta[k]['name']} ({prompts_meta[k]['category']})"
        )
    with c_sel2:
        compare_mode = st.radio(
            "Comparison Layout:",
            ["Compare All 3 Models", "Pairwise Comparison (Pick 2 Models)"],
            horizontal=True
        )

    p_info = prompts_meta[selected_pid]
    p_scores = prompt_metrics.get(selected_pid, {}).get("models", {})
    obs = qualitative_notes.get(selected_pid, {}).get("observations", {})

    st.info(f"**Target Prompt:** \"{p_info['prompt_text']}\"")

    if compare_mode == "Compare All 3 Models":
        selected_models = ["Model A", "Model B", "Model C"]
    else:
        m_sel1, m_sel2 = st.columns(2)
        with m_sel1:
            m1 = st.selectbox("Left Model:", ["Model A", "Model B", "Model C"], index=0)
        with m_sel2:
            m2 = st.selectbox("Right Model:", ["Model A", "Model B", "Model C"], index=1)
        selected_models = [m1, m2]

    # Render image columns
    cols = st.columns(len(selected_models))

    for idx, mid in enumerate(selected_models):
        with cols[idx]:
            m_spec = models_meta.get(mid, {})
            label = get_model_label(mid, models_meta, disclose)
            img_path = p_info["images"][mid]
            img = get_image(img_path)
            score_data = p_scores.get(mid, {})
            m_obs = obs.get(mid, {})

            st.markdown(f"### {mid}")
            st.markdown(f"**Provider:** {m_spec.get('company')} · **Model:** `{m_spec.get('model_name')}`")

            if img:
                st.image(img, use_container_width=True)
                st.caption(f"Native Resolution: {img.size[0]}×{img.size[1]} px · Format: {img.format}")
            else:
                st.error("Image file not found.")

            # Inspection Card
            st.markdown(
                f"""
                <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:12px; margin-top:10px;">
                    <div style="font-size:0.85rem; font-weight:700; color:#1E3A8A; margin-bottom:6px;">
                        Overall Score: {score_data.get('overall', 0):.2f} / 5.00
                    </div>
                    <div style="font-size:0.8rem; color:#475569; line-height:1.5;">
                        • Prompt Adherence: <strong>{score_data.get('prompt_adherence', 0):.2f}</strong><br>
                        • Visual Quality: <strong>{score_data.get('visual_quality', 0):.2f}</strong><br>
                        • Indian Authenticity: <strong>{score_data.get('indian_authenticity', 0):.2f}</strong><br>
                        • Evaluator Disagreement: <strong>±{score_data.get('overall_std', 0):.2f}</strong>
                    </div>
                    <hr style="margin:8px 0; border:0; border-top:1px solid #E2E8F0;">
                    <div style="font-size:0.75rem; color:#334155;">
                        <strong>Aspect Ratio & Layout:</strong><br>{m_obs.get('aspect_ratio', 'N/A')}
                    </div>
                    <div style="font-size:0.75rem; color:#334155; margin-top:4px;">
                        <strong>Key Visual Trait:</strong><br>{m_obs.get('visual_strengths', '')[:120]}...
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
