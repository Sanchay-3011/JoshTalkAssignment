"""
Scaling Proposal & Architecture page for Josh Talks AI evaluation.
Product roadmap for expanding from small pilot to nationwide foundation model benchmarking.
"""

import streamlit as st


def render_scaling_plan(ctx: dict):
    st.markdown("## 📈 PRODUCT SCALING PROPOSAL & ROADMAP")
    st.markdown(
        "<div style='font-size:1.0rem; color:#475569; margin-top:-8px; margin-bottom:20px;'>"
        "How Josh Talks AI can scale this prototype into India's premier generative vision evaluation standard."
        "</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Phase 1: Expansion of Prompts & Cultural Nuance")
        st.markdown(
            """
            - **Scale from 5 to 100+ Prompts**: Cover deep regional Indian e-commerce verticals:
              - *Bridal & Haute Couture*: Kanjeevaram silk, Paithani sarees, Chaniya cholis, Bandhani lehengas.
              - *Handicrafts & Artisans*: Kashmiri pashmina, Kolhapuri leather chappals, Moradabad brassware, Blue pottery of Jaipur.
              - *FMCG & Ayurveda*: Ayurvedic skin oils, regional masala spice blends, organic millet snacks.
            - **Multilingual Prompt Ingestion**: Test model response to native Indian language prompts (Hindi, Tamil, Telugu, Bengali) and Hinglish phrasing commonly typed by D2C merchants.
            - **Multi-Seed Generation Testing**: Generate 5 randomized seeds per prompt per model to quantify within-model variance, rather than judging a model on a single lucky or unlucky output.
            """
        )

        st.markdown("### Phase 2: Rater Workforce & Demographic Stratification")
        st.markdown(
            """
            - **Scale Evaluators from 10 to 100+**: Leverage the **Josh Jobs** contributor network (20,000+ active freelance workers across Tier-2/3 India).
            - **Geographic & Regional Stratification**: Ensure evaluators rating Kanjeevaram sarees represent South Indian states, while evaluators rating Chanderi sarees represent Central/North India.
            - **Honeypot & Trap Tasks**: Automatically inject known good and intentionally corrupted images into evaluator queues to detect inattentive raters, click-fraud, or speedrunning.
            """
        )

    with col2:
        st.markdown("### Phase 3: Hybrid Human + Multimodal AI Evaluation")
        st.markdown(
            """
            - **Two-Tier Evaluation Funnel**:
              1. **Tier 1 (High-Throughput Vision-LLM Judge)**: Use SOTA multimodal models (e.g. GPT-4o / Gemini 1.5 Pro) with structured rubrics to screen 10,000+ candidate generations for obvious anatomical deformities, blurriness, and text prompt alignment.
              2. **Tier 2 (Human Cultural Verification)**: Route top-performing candidate images to human raters on Josh Jobs for subjective cultural resonance, regional appropriateness, and commercial appeal.
            - **New Evaluated Dimension: `commercial_usefulness`**:
              Add explicit business metrics rated by e-commerce marketing managers (e.g., *Is the product distinguishable for 1-click buy? Can text overlays be inserted?*).
            """
        )

        st.markdown("### Phase 4: Enterprise E-Commerce Elo Arena")
        st.markdown(
            """
            - **Blind Pairwise Battles (Elo Rating)**: Transition from independent 1-5 Likert scales to blind side-by-side A/B battles (similar to LMSYS Chatbot Arena).
            - **Live D2C Brand Integrations**: Allow Indian fashion brands (e.g., Fabindia, Manyavar, Meesho sellers) to submit their seasonal catalogs as private benchmark suites.
            - **Continuous Model Version Regression Tracking**: Automatically trigger benchmark evaluation suites whenever OpenAI, Google, Midjourney, or FLUX release model checkpoints.
            """
        )

    st.markdown("---")

    # Scaled System Architecture Diagram
    st.markdown("### 🏛️ Target Scaled System Architecture")
    st.markdown(
        """
        ```mermaid
        flowchart LR
            subgraph Ingestion
                P[Regional Prompt Bank\n25+ Indian Languages]
                B[Josh Jobs Rater Pool\nTier-2/3 Demographics]
            end

            subgraph Generation_Engine
                MR[Unified Multi-Model Runner]
                OA[OpenAI ChatGPT Images 2.5]
                G3[Gemini 3.1 Pro]
                GF[Gemini Flash]
                FL[FLUX 1.1 Pro]
            end

            subgraph Evaluation_Funnel
                VLLM[Tier 1: Vision LLM Judge\nQuality & Safety Screen]
                HR[Tier 2: Josh Jobs Raters\nCultural & Commercial Fit]
            end

            subgraph Analytics
                ELO[Elo Arena Leaderboard]
                REG[Regression Alerts]
                API[D2C Brand Enterprise API]
            end

            P --> MR
            MR --> OA & G3 & GF & FL
            OA & G3 & GF & FL --> VLLM
            VLLM -->|Filter Top 20%| HR
            B --> HR
            HR --> ELO
            ELO --> REG & API
        ```
        """
    )
