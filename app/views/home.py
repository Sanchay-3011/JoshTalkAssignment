"""
Homepage for India Image Eval.
Clean product landing page presenting two primary pathways:
1. Assignment Evaluation (view completed benchmark results)
2. Try the Rating App (Beta participant rating prototype)
"""

import streamlit as st


def render_home():
    # Subtle top pill badge
    st.markdown(
        """
        <div style="text-align: center; margin-top: 25px; margin-bottom: 12px;">
            <span style="
                background: #F1F5F9;
                color: #475569;
                font-size: 0.78rem;
                font-weight: 600;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                padding: 6px 14px;
                border-radius: 9999px;
                border: 1px solid #E2E8F0;
                display: inline-block;
            ">
                Foundation Model Evaluation · Indian E-Commerce
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Main Title & Subtitle
    st.markdown(
        """
        <div style="text-align: center; max-width: 820px; margin: 0 auto 36px auto;">
            <h1 style="
                font-size: 2.75rem;
                font-weight: 800;
                color: #0F172A;
                letter-spacing: -0.03em;
                line-height: 1.15;
                margin-bottom: 12px;
            ">
                INDIA IMAGE EVAL
            </h1>
            <p style="
                font-size: 1.25rem;
                font-weight: 500;
                color: #334155;
                line-height: 1.4;
                margin-bottom: 18px;
            ">
                Human evaluation of text-to-image models for Indian e-commerce.
            </p>
            <p style="
                font-size: 0.98rem;
                color: #64748B;
                line-height: 1.6;
                margin: 0 auto;
                max-width: 680px;
            ">
                This project evaluates how well leading image generation models handle Indian e-commerce scenarios using human judgment across prompt adherence, visual quality, and Indian audience authenticity.
            </p>
            <p style="
                font-size: 0.92rem;
                color: #475569;
                line-height: 1.5;
                margin-top: 14px;
                font-weight: 500;
            ">
                Explore the results of the completed evaluation or try the prototype rating experience used to demonstrate how this evaluation could work at scale.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    # Two Primary Option Cards
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
            <div style="
                background: #FFFFFF;
                border: 1px solid #E2E8F0;
                border-radius: 14px;
                padding: 32px 28px 24px 28px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                min-height: 330px;
            ">
                <div>
                    <div style="font-size: 2.2rem; margin-bottom: 14px;">📊</div>
                    <div style="font-size: 1.28rem; font-weight: 700; color: #0F172A; margin-bottom: 4px;">
                        ASSIGNMENT EVALUATION
                    </div>
                    <div style="font-size: 0.88rem; font-weight: 600; color: #2563EB; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.04em;">
                        Explore the Results
                    </div>
                    <p style="font-size: 0.92rem; color: #475569; line-height: 1.55; margin-bottom: 24px;">
                        View the completed evaluation, including model rankings, prompt-level findings, participant ratings, visual comparisons, methodology, and key conclusions.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
        if st.button("VIEW ASSIGNMENT RESULTS →", key="btn_view_results", use_container_width=True, type="primary"):
            st.session_state["view"] = "assignment_results"
            st.rerun()

    with col2:
        st.markdown(
            """
            <div style="
                background: #FFFFFF;
                border: 1px solid #E2E8F0;
                border-radius: 14px;
                padding: 32px 28px 24px 28px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                min-height: 330px;
            ">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 14px;">
                        <span style="font-size: 2.2rem;">🧪</span>
                        <span style="
                            background: #FEF3C7;
                            color: #92400E;
                            font-size: 0.74rem;
                            font-weight: 700;
                            letter-spacing: 0.08em;
                            padding: 3px 9px;
                            border-radius: 6px;
                            border: 1px solid #FDE68A;
                        ">BETA</span>
                    </div>
                    <div style="font-size: 1.28rem; font-weight: 700; color: #0F172A; margin-bottom: 4px;">
                        TRY THE RATING APP
                    </div>
                    <div style="font-size: 0.88rem; font-weight: 600; color: #D97706; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.04em;">
                        Participate in a Sample Evaluation
                    </div>
                    <p style="font-size: 0.92rem; color: #475569; line-height: 1.55; margin-bottom: 24px;">
                        Try the participant-facing prototype. Enter your details, review the generated images, and rate them across the evaluation dimensions.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
        if st.button("TRY RATING APP →", key="btn_try_rating", use_container_width=True, type="secondary"):
            st.session_state["view"] = "try_rating_app"
            st.rerun()

    # Clear prototype disclaimer below the cards
    st.markdown(
        """
        <div style="
            text-align: center;
            max-width: 650px;
            margin: 44px auto 20px auto;
            padding: 14px 18px;
            background: #F8FAFC;
            border-radius: 8px;
            border: 1px dashed #CBD5E1;
            color: #64748B;
            font-size: 0.82rem;
            line-height: 1.5;
        ">
            <strong>Prototype Note:</strong> The Rating App is a functional prototype demonstrating how Josh Talks could operationalize human-in-the-loop image evaluation at scale. Submissions made in the prototype are stored separately and do not alter the verified 11-participant assignment survey dataset.
        </div>
        """,
        unsafe_allow_html=True
    )
