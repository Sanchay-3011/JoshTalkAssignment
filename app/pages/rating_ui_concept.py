"""
Product Concept: Human Evaluation Rating UI & Enterprise Evaluation Engine.
Demonstrates the prototype rater workflow for internal AI labs and product teams.
"""

import streamlit as st
from app.config import get_image


def render_rating_ui_concept(ctx: dict):
    prompts_meta = ctx["prompts_meta"]

    st.markdown("## 💻 EVALUATION PRODUCT CONCEPT: HUMAN RATING INTERFACE")
    st.markdown(
        "<div style='font-size:1.0rem; color:#475569; margin-top:-8px; margin-bottom:20px;'>"
        "Interactive prototype of the proprietary blind evaluation interface that human raters interact with on the Josh Talks platform."
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background:#FEF3C7; border:1px solid #FDE68A; border-radius:8px; padding:12px 16px; margin-bottom:20px;">
            <strong style="color:#92400E;">⚡ Interactive Product Prototype:</strong>
            <span style="font-size:0.88rem; color:#78350F;">
                This conceptual interface illustrates how internal AI evaluation teams, freelance raters, or D2C catalog editors
                grade model outputs blindly in real-time. Submissions here do not alter the historical survey evidence.
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    p_keys = list(prompts_meta.keys())
    sel_pid = st.selectbox(
        "Select Active Evaluation Task:",
        p_keys,
        format_func=lambda k: f"{prompts_meta[k]['name']} — {prompts_meta[k]['category']}"
    )
    p_info = prompts_meta[sel_pid]

    st.markdown(
        f"""
        <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-radius:10px; padding:16px; margin-bottom:20px;">
            <div style="font-size:0.75rem; font-weight:700; color:#64748B;">PROMPT TO EVALUATE</div>
            <div style="font-size:1.05rem; font-weight:700; color:#0F172A; margin-top:4px;">
                "{p_info['prompt_text']}"
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 3-Column Blind Rating Interface
    colA, colB, colC = st.columns(3)
    models = [("Model A", colA), ("Model B", colB), ("Model C", colC)]

    user_ratings = {}

    for mid, col in models:
        with col:
            st.markdown(f"### Image {mid[-1]}")
            st.caption("Blind Label: Provider Masked")

            img_path = p_info["images"][mid]
            img = get_image(img_path)
            if img:
                st.image(img, use_container_width=True)

            st.markdown("---")
            st.markdown(f"**Rate Image {mid[-1]}:**")

            q1 = st.slider(
                f"1. Prompt Adherence ({mid})",
                min_value=1, max_value=5, value=4,
                help="How well does this image faithfully match the text prompt?",
                key=f"mock_pa_{mid}"
            )
            q2 = st.slider(
                f"2. Visual Quality ({mid})",
                min_value=1, max_value=5, value=4,
                help="How sharp, realistic, and defect-free is the rendering?",
                key=f"mock_vq_{mid}"
            )
            q3 = st.slider(
                f"3. Indian Cultural Authenticity ({mid})",
                min_value=1, max_value=5, value=4,
                help="Does this feel culturally authentic and appropriate for Indian audiences?",
                key=f"mock_ia_{mid}"
            )

            user_ratings[mid] = round((q1 + q2 + q3) / 3.0, 2)
            st.metric(f"Computed Score ({mid[-1]})", f"{user_ratings[mid]} / 5.0")

    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    if st.button("🚀 Submit Mock Rating Batch", type="primary"):
        st.success(
            f"Mock Batch Submitted Successfully! Synthetic Scores: "
            f"Image A = {user_ratings['Model A']} | Image B = {user_ratings['Model B']} | Image C = {user_ratings['Model C']}. "
            f"In production, this event streams into the Aggregation Engine and updates the live E-Commerce Leaderboard."
        )

    st.markdown("---")

    # Enterprise Evaluation Engine Architecture
    st.markdown("### 🏗️ Enterprise Evaluation Engine Workflow")
    st.markdown(
        """
        How an AI research lab building foundation models for India (e.g., Josh Talks AI, Sarvam, or BharatGPT)
        operationalizes this human-in-the-loop evaluation framework at scale:
        """
    )

    st.markdown(
        """
        ```mermaid
        graph TD
            A[1. Prompt Library] -->|Curated Indian Catalog Prompts| B[2. Unified Model Runner]
            B -->|Batch API Calls| C1[OpenAI GPT Image 1]
            B -->|Batch API Calls| C2[Google Gemini 3.1 Pro]
            B -->|Batch API Calls| C3[Google Gemini 3.5 Flash]
            C1 --> D[3. Blind Randomizer]
            C2 --> D
            C3 --> D
            D -->|Randomized Position & Masked Labels| E[4. Human Rating Interface]
            E -->|1-5 Likert Criteria + Consent| F[5. Aggregation & Verification Engine]
            F -->|Inter-Rater Consensus Check| G[6. Model Leaderboard]
            F -->|Flag Low Agreement / Outliers| H[7. Reviewer Quality Control]
            G --> I[8. Enterprise Product Decision Dashboard]
        ```
        """
    )

    st.markdown(
        r"""
        #### Key Platform Advantages:
        1. **Elimination of Brand Prestige Bias:** Randomizes presentation order (A/B/C) per rater per prompt to neutralize primacy effects.
        2. **Multi-Rater Consensus Verification:** Calculates real-time inter-rater agreement (Krippendorff's Alpha); flags raters who speedrun or disagree systematically with ground truth controls.
        3. **Automated Deployment Gates:** Provides an API endpoint that blocks production catalog generation unless the model passes a minimum cultural authenticity threshold ($\ge 4.5/5.0$).
        """
    )
