"""
Reports and Reflections page for Josh Talks AI evaluation.
Displays the full submission document, one-page executive brief, and answers to the 5 reflections.
"""

import os
import streamlit as st

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")


def render_reports_page(ctx: dict):
    st.markdown("## 📄 ASSIGNMENT SUBMISSION REPORTS & REFLECTIONS")
    st.markdown(
        "<div style='font-size:1.0rem; color:#475569; margin-top:-8px; margin-bottom:20px;'>"
        "Official submission documents, executive one-page brief, and strategic evaluation reflections."
        "</div>",
        unsafe_allow_html=True
    )

    tab1, tab2, tab3 = st.tabs([
        "1. Executive Brief (1-Page Summary)",
        "2. Main Comprehensive Evaluation Report",
        "3. Final Reflections (The 5 Mandatory Questions)"
    ])

    exec_path = os.path.join(REPORTS_DIR, "executive_summary.md")
    main_path = os.path.join(REPORTS_DIR, "main_evaluation_report.md")

    with tab1:
        if os.path.exists(exec_path):
            with open(exec_path, "r", encoding="utf-8") as f:
                exec_text = f.read()
            st.markdown(exec_text)
            st.download_button(
                label="📥 Download Executive Summary (.md)",
                data=exec_text,
                file_name="executive_summary.md",
                mime="text/markdown"
            )
        else:
            st.info("Executive summary file is being generated...")

    with tab2:
        if os.path.exists(main_path):
            with open(main_path, "r", encoding="utf-8") as f:
                main_text = f.read()
            st.markdown(main_text)
            st.download_button(
                label="📥 Download Main Evaluation Report (.md)",
                data=main_text,
                file_name="main_evaluation_report.md",
                mime="text/markdown"
            )
        else:
            st.info("Main evaluation report is being generated...")

    with tab3:
        st.markdown("### Strategic Reflections for Josh Talks AI Leadership")

        st.markdown(
            """
            #### 1. Why did you choose this eval?
            E-commerce product visual generation is the single largest near-term commercial application of text-to-image foundation models in India. Millions of small MSME sellers, D2C fashion brands, and regional artisans on platforms like Meesho, Flipkart, and Myntra face prohibitive costs (₹50,000–₹2,00,000 per shoot) for studio photography with human models, mannequins, and lighting setups. Evaluating whether state-of-the-art AI can replace or augment professional studio photography with authentic Indian cultural context directly addresses a massive, high-impact economic bottleneck.

            #### 2. Why is it useful for India?
            Western foundation models are heavily trained on European and North American visual cultures (e.g. suits, Western dresses, suburban kitchens). When prompted for Indian items, models frequently commit subtle or severe cultural errors—conflating a sleeveless Nehru jacket with a full-sleeved European tuxedo, rendering generic orientalist decor, or failing to grasp the pleats of a Banarasi silk saree. This evaluation explicitly measures whether foundation models respect nuanced Indian sartorial, festive, and household conventions, ensuring technology deployed in India actually works for Indian citizens.

            #### 3. Why would an AI lab building for India care about it?
            An AI lab (such as Josh Talks AI, Sarvam AI, or enterprise LLM/VL developers) cannot rely on generic ImageNet or Western benchmarks (like MS-COCO or GenEval) to evaluate visual models for Indian deployment. A model might achieve a 90+ aesthetic score on Western prompts while completely failing on Indian ethnic garments or festive packaging. Having an empirical, human-grounded benchmark provides labs with the exact training signal, RLHF preference data, and fine-tuning guidance needed to build culturally competitive visual AI products.

            #### 4. What did you learn from running the sample?
            - **Model A (OpenAI GPT Image 1) possesses a native grasp of commercial intent**: It did not just draw the requested items; it structured them as production-ready ad creatives with authentic typography, feature badges, and complementary props (e.g., matching pearl jewelry on the saree mannequin and home-cooked Indian foods inside the tiffin tiers).
            - **Cultural authenticity tracks general coherence**: Contrary to the hypothesis that an image might be technically sharp yet culturally inaccurate, evaluators showed that cultural errors (e.g. Model C's wooden dummy mannequin or full-sleeved Bandhgala) directly crashed visual quality and prompt adherence scores in tandem.
            - **Model C is polarized, not simply mediocre**: With an average standard deviation of 1.35 (vs 0.58 for Model A), evaluators deeply disagreed on Model C's outputs, indicating a high-variance, hit-or-miss generation model that lacks enterprise reliability.

            #### 5. What would you improve with more time?
            - **Randomized Presentation Order**: To fully rule out primacy bias (since Model A was listed first in the Google Form), I would implement real-time dynamic Latin-square randomization of image order per evaluator per prompt.
            - **Expanded Rater Cohort**: Scale from 10 participants to 50+ stratified by regional geography (evaluating South Indian attire with South Indian raters) and age demographics.
            - **Pairwise Elo Arena Battles**: Transition from independent 1-5 Likert scales to blind A/B head-to-head comparisons, which eliminate individual rater scale calibration differences.
            - **Multi-Seed Stability Testing**: Run 5 distinct generation seeds per prompt per model to quantify whether Model C's failures were unlucky outlier generations or systemic model flaws.
            """
        )
