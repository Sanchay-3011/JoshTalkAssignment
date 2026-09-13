"""
Homepage for India Image Eval.
Exact 1:1 match to product design specification with complete dark mode immunity.
"""

import streamlit as st


def render_home():
    # Top Right "View on GitHub" Link
    st.markdown(
        """
        <div style="display: flex; justify-content: flex-end; align-items: center; margin-top: -14px; margin-bottom: 8px;">
            <a href="https://github.com/Sanchay-3011/JoshTalkAssignment" target="_blank" style="
                display: inline-flex;
                align-items: center;
                gap: 7px;
                color: #0F172A;
                text-decoration: none;
                font-size: 0.88rem;
                font-weight: 600;
                transition: opacity 0.15s ease;
            ">
                <svg height="19" width="19" viewBox="0 0 16 16" fill="#0F172A">
                    <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
                View on GitHub
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Pill Badge: FOUNDATION MODEL EVALUATION
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 12px;">
            <span style="
                background: #EFF6FF;
                color: #2563EB;
                font-size: 0.72rem;
                font-weight: 700;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                padding: 5px 16px;
                border-radius: 9999px;
                display: inline-block;
            ">
                FOUNDATION MODEL EVALUATION
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Hero Title, Subtitle & Description
    st.markdown(
        """
        <div style="text-align: center; max-width: 860px; margin: 0 auto;">
            <h1 style="
                font-size: 2.85rem;
                font-weight: 800;
                color: #0F172A;
                letter-spacing: -0.025em;
                line-height: 1.15;
                margin-top: 0;
                margin-bottom: 10px;
            ">
                INDIA <span style="color: #2563EB;">IMAGE EVAL</span>
            </h1>
            <p style="
                font-size: 1.12rem;
                font-weight: 500;
                color: #334155;
                line-height: 1.4;
                margin-bottom: 10px;
            ">
                Human evaluation of text-to-image models for Indian e-commerce.
            </p>
            <p style="
                font-size: 0.92rem;
                color: #64748B;
                line-height: 1.55;
                margin: 0 auto;
                max-width: 740px;
            ">
                This project evaluates how well leading image generation models handle Indian e-commerce scenarios using human judgment across prompt adherence, visual quality, and Indian audience authenticity.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Indian Tricolor Divider
    st.markdown(
        """
        <div style="display: flex; justify-content: center; margin: 14px auto 24px auto; width: 84px;">
            <div style="background: #F97316; width: 28px; height: 4px; border-radius: 4px 0 0 4px;"></div>
            <div style="background: #CBD5E1; width: 28px; height: 4px;"></div>
            <div style="background: #16A34A; width: 28px; height: 4px; border-radius: 0 4px 4px 0;"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Two Option Cards Layout
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        with st.container(border=True):
            st.markdown(
                """
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                    <div style="background: #EFF6FF; width: 44px; height: 44px; border-radius: 10px; display: flex; align-items: center; justify-content: center;">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="#2563EB">
                            <rect x="3" y="12" width="4" height="8" rx="1"/>
                            <rect x="10" y="7" width="4" height="13" rx="1"/>
                            <rect x="17" y="3" width="4" height="17" rx="1"/>
                        </svg>
                    </div>
                    <span style="
                        background: #EFF6FF;
                        color: #2563EB;
                        font-size: 0.70rem;
                        font-weight: 700;
                        letter-spacing: 0.06em;
                        padding: 4px 10px;
                        border-radius: 9999px;
                        border: 1px solid #BFDBFE;
                    ">
                        🏆 COMPLETED
                    </span>
                </div>
                <div style="font-size: 1.25rem; font-weight: 800; color: #0F172A; margin-bottom: 2px; letter-spacing: -0.01em;">
                    ASSIGNMENT EVALUATION
                </div>
                <div style="font-size: 0.95rem; font-weight: 700; color: #2563EB; margin-bottom: 10px;">
                    Explore the Results
                </div>
                <p style="font-size: 0.86rem; color: #64748B; line-height: 1.5; min-height: 60px; margin-bottom: 18px;">
                    View the completed evaluation, including model rankings, prompt-level findings, participant ratings, visual comparisons, methodology, and key conclusions.
                </p>
                """,
                unsafe_allow_html=True
            )
            if st.button("View Assignment Results →", key="btn_view_results", use_container_width=True):
                st.session_state["view"] = "assignment_results"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.markdown(
                """
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                    <div style="background: #FFF7ED; width: 44px; height: 44px; border-radius: 10px; display: flex; align-items: center; justify-content: center;">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#EA580C" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M10 2v7.31L4.69 18.2A2 2 0 0 0 6.4 21h11.2a2 2 0 0 0 1.71-2.8L14 9.31V2h-4Z"/>
                            <path d="M8.5 2h7"/>
                            <path d="M7 16h10"/>
                        </svg>
                    </div>
                    <span style="
                        background: #FFEDD5;
                        color: #EA580C;
                        font-size: 0.70rem;
                        font-weight: 700;
                        letter-spacing: 0.06em;
                        padding: 4px 10px;
                        border-radius: 9999px;
                        border: 1px solid #FED7AA;
                    ">
                        BETA
                    </span>
                </div>
                <div style="font-size: 1.25rem; font-weight: 800; color: #0F172A; margin-bottom: 2px; letter-spacing: -0.01em;">
                    TRY THE RATING APP
                </div>
                <div style="font-size: 0.95rem; font-weight: 700; color: #EA580C; margin-bottom: 10px;">
                    Participate in a Sample Evaluation
                </div>
                <p style="font-size: 0.86rem; color: #64748B; line-height: 1.5; min-height: 60px; margin-bottom: 18px;">
                    Try the participant-facing prototype. Enter your details, review the generated images, and rate them across the evaluation dimensions.
                </p>
                """,
                unsafe_allow_html=True
            )
            if st.button("Try Rating App (Beta) →", key="btn_try_rating", use_container_width=True):
                st.session_state["view"] = "try_rating_app"
                st.rerun()

    # Bottom Full-Width Disclaimer Box
    st.markdown(
        """
        <div style="
            background: #F0FDF4;
            border: 1px solid #BBF7D0;
            border-radius: 12px;
            padding: 12px 18px;
            margin: 22px auto 0 auto;
            display: flex;
            align-items: center;
            gap: 16px;
        ">
            <div style="
                background: #16A34A;
                width: 30px;
                height: 30px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                flex-shrink: 0;
                color: white;
            ">
                <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"/>
                </svg>
            </div>
            <div style="
                width: 1px;
                height: 34px;
                background-color: #BBF7D0;
                flex-shrink: 0;
            "></div>
            <div style="display: flex; flex-direction: column; gap: 2px;">
                <div style="color: #15803D; font-weight: 700; font-size: 0.84rem;">
                    Note: This rating app is a prototype and separate from the completed survey dataset used for the assignment results.
                </div>
                <div style="color: #166534; font-size: 0.80rem; line-height: 1.4;">
                    The assignment results are based on 11 survey responses (10 primary participants + 1 robustness check) collected via Google Forms.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
