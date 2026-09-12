"""
Try Rating App (BETA) - Interactive Human Evaluation Prototype.
Demonstrates how Josh Talks could operationalize human-in-the-loop image evaluation at scale.
Participant responses are stored in data/beta_responses/ and are completely isolated
from the verified 11-participant assignment survey dataset.
"""

import os
import json
import random
import re
from datetime import datetime
import pandas as pd
import streamlit as st
from app.config import get_image

BETA_DATA_DIR = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")), "data", "beta_responses")
BETA_JSON_FILE = os.path.join(BETA_DATA_DIR, "beta_submissions.json")
BETA_CSV_FILE = os.path.join(BETA_DATA_DIR, "beta_submissions.csv")


def init_beta_state(prompts_meta: dict):
    if "beta_step" not in st.session_state:
        st.session_state["beta_step"] = "details"  # "details", "eval", "complete"
    if "beta_prompt_idx" not in st.session_state:
        st.session_state["beta_prompt_idx"] = 0  # 0 to 4
    if "beta_participant" not in st.session_state:
        st.session_state["beta_participant"] = {
            "name": "",
            "email": "",
            "age": 24,
            "consent": False
        }
    if "beta_ratings" not in st.session_state:
        st.session_state["beta_ratings"] = {}
    if "beta_blind_mapping" not in st.session_state:
        # Create randomized blind mapping per prompt for this session
        mapping = {}
        for p_key in ["P1", "P2", "P3", "P4", "P5"]:
            models = ["Model A", "Model B", "Model C"]
            random.shuffle(models)
            mapping[p_key] = {
                "Image A": models[0],
                "Image B": models[1],
                "Image C": models[2]
            }
        st.session_state["beta_blind_mapping"] = mapping


def is_valid_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email.strip()))


def save_beta_submission():
    os.makedirs(BETA_DATA_DIR, exist_ok=True)
    participant = st.session_state["beta_participant"]
    ratings = st.session_state["beta_ratings"]
    blind_map = st.session_state["beta_blind_mapping"]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    submission_id = f"BETA_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    record = {
        "submission_id": submission_id,
        "timestamp": timestamp,
        "participant": participant,
        "ratings": ratings,
        "blind_mapping": blind_map
    }

    # Save to JSON
    submissions = []
    if os.path.exists(BETA_JSON_FILE):
        try:
            with open(BETA_JSON_FILE, "r", encoding="utf-8") as f:
                submissions = json.load(f)
        except Exception:
            submissions = []
    submissions.append(record)
    with open(BETA_JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(submissions, f, indent=2)

    # Flatten and append to CSV
    csv_rows = []
    for p_key, img_ratings in ratings.items():
        for label, scores in img_ratings.items():
            actual_model = blind_map.get(p_key, {}).get(label, "Unknown")
            csv_rows.append({
                "submission_id": submission_id,
                "timestamp": timestamp,
                "participant_name": participant["name"],
                "participant_email": participant["email"],
                "participant_age": participant["age"],
                "prompt_id": p_key,
                "display_label": label,
                "underlying_model": actual_model,
                "prompt_adherence": scores.get("adherence", 3),
                "visual_quality": scores.get("quality", 3),
                "indian_authenticity": scores.get("authenticity", 3)
            })

    df_new = pd.DataFrame(csv_rows)
    if os.path.exists(BETA_CSV_FILE):
        df_new.to_csv(BETA_CSV_FILE, mode="a", header=False, index=False)
    else:
        df_new.to_csv(BETA_CSV_FILE, mode="w", header=True, index=False)


def render_try_rating_app(context: dict):
    prompts_meta = context["prompts_meta"]
    init_beta_state(prompts_meta)

    # Top Navigation Bar
    top_col1, top_col2 = st.columns([1, 4])
    with top_col1:
        if st.button("← Back to Home", key="beta_btn_back_home"):
            st.session_state["view"] = "home"
            st.rerun()

    st.markdown("<hr style='margin: 12px 0 20px 0;'>", unsafe_allow_html=True)

    # Header & Prototype Notice
    st.markdown(
        """
        <div>
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
                <h2 style="font-size: 2rem; font-weight: 800; color: #0F172A; margin: 0;">
                    TRY THE RATING APP
                </h2>
                <span style="
                    background: #FEF3C7;
                    color: #92400E;
                    font-size: 0.78rem;
                    font-weight: 700;
                    padding: 3px 10px;
                    border-radius: 6px;
                    border: 1px solid #FDE68A;
                ">BETA</span>
            </div>
            <p style="font-size: 0.95rem; color: #475569; margin-bottom: 16px;">
                Interactive prototype demonstrating the contributor-facing rating experience.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Prototype isolation warning
    st.markdown(
        """
        <div style="
            background: #FFFBEB;
            border-left: 4px solid #F59E0B;
            border-radius: 0 8px 8px 0;
            padding: 12px 16px;
            margin-bottom: 24px;
            font-size: 0.86rem;
            color: #92400E;
            line-height: 1.5;
        ">
            <strong>Prototype Notice:</strong> This rating experience demonstrates how the evaluation could be run as an independent product. Submissions made here are stored separately in <code>data/beta_responses/</code> and will <strong>not</strong> alter the completed 11-participant assignment survey results.
        </div>
        """,
        unsafe_allow_html=True
    )

    prompt_keys = ["P1", "P2", "P3", "P4", "P5"]

    # STAGE 1: PARTICIPANT DETAILS & CONSENT
    if st.session_state["beta_step"] == "details":
        st.markdown("### 📋 Step 1: Contributor Details & Consent")
        st.markdown("Please provide your details before entering the evaluation workspace:")

        with st.form("beta_details_form"):
            name = st.text_input("Full Name *", value=st.session_state["beta_participant"]["name"], placeholder="e.g. Priya Sharma")
            email = st.text_input("Email Address *", value=st.session_state["beta_participant"]["email"], placeholder="e.g. priya@example.com")
            age = st.number_input("Age *", min_value=1, max_value=100, value=int(st.session_state["beta_participant"]["age"]))

            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
            st.markdown("##### 📜 Informed Consent Clause")
            consent_text = (
                "I confirm that I am 18 years or older. I voluntarily participated in this evaluation. "
                "I consent to my name, email, and responses/ratings being included in this assignment submission for hiring evaluation purposes."
            )
            st.markdown(
                f"""
                <div style="background:#F8FAFC; border:1px solid #E2E8F0; padding:12px 14px; border-radius:6px; font-size:0.84rem; color:#475569; margin-bottom:12px;">
                    <em>"{consent_text}"</em>
                </div>
                """,
                unsafe_allow_html=True
            )

            consent_checked = st.checkbox("I have read and affirmatively agree to the consent clause above *", value=st.session_state["beta_participant"]["consent"])

            st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
            submit_details = st.form_submit_button("START EVALUATION →", type="primary", use_container_width=True)

            if submit_details:
                errors = []
                if not name.strip():
                    errors.append("Please enter your Full Name.")
                if not email.strip() or not is_valid_email(email):
                    errors.append("Please enter a valid Email Address.")
                if age < 18:
                    errors.append("You must be 18 years of age or older to participate.")
                if not consent_checked:
                    errors.append("You must affirmatively agree to the informed consent clause.")

                if errors:
                    for err in errors:
                        st.error(f"⚠️ {err}")
                else:
                    st.session_state["beta_participant"] = {
                        "name": name.strip(),
                        "email": email.strip(),
                        "age": age,
                        "consent": True
                    }
                    st.session_state["beta_step"] = "eval"
                    st.session_state["beta_prompt_idx"] = 0
                    st.rerun()

    # STAGE 2: IMAGE EVALUATION FLOW (5 PROMPTS)
    elif st.session_state["beta_step"] == "eval":
        idx = st.session_state["beta_prompt_idx"]
        p_key = prompt_keys[idx]
        p_data = prompts_meta[p_key]
        blind_map = st.session_state["beta_blind_mapping"][p_key]

        # Progress bar & Step indicator
        progress_val = (idx + 1) / 5.0
        st.progress(progress_val)
        st.markdown(
            f"""
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                <span style="font-weight:700; color:#1E3A8A; font-size:1.05rem;">
                    Prompt {idx + 1} of 5: {p_data.get('name', '')}
                </span>
                <span style="font-size:0.85rem; color:#64748B;">
                    {int(progress_val * 100)}% Completed
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Exact prompt string
        st.markdown(
            f"""
            <div style="background:#F8FAFC; border-left:4px solid #3B82F6; padding:14px 18px; border-radius:0 8px 8px 0; margin-bottom:24px;">
                <div style="font-size:0.75rem; font-weight:700; color:#64748B; text-transform:uppercase;">
                    Target E-Commerce Catalog Prompt:
                </div>
                <div style="font-size:1rem; font-weight:600; color:#0F172A; margin:6px 0;">
                    "{p_data.get('prompt_text', '')}"
                </div>
                <div style="font-size:0.8rem; color:#64748B;">
                    Rate each of the 3 candidate images below across the standard 1–5 criteria. Models are blinded as Image A, Image B, Image C.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Initialize storage for this prompt if not present
        if p_key not in st.session_state["beta_ratings"]:
            st.session_state["beta_ratings"][p_key] = {}

        cols = st.columns(3, gap="medium")
        display_labels = ["Image A", "Image B", "Image C"]

        for d_label, col in zip(display_labels, cols):
            actual_model = blind_map[d_label]
            img_rel_path = p_data["images"].get(actual_model, "")
            img_obj = get_image(img_rel_path)

            current_scores = st.session_state["beta_ratings"].get(p_key, {}).get(d_label, {
                "adherence": 4,
                "quality": 4,
                "authenticity": 4
            })

            with col:
                st.markdown(
                    f"""
                    <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:12px; margin-bottom:12px; text-align:center;">
                        <span style="font-weight:700; font-size:1.1rem; color:#0F172A;">{d_label}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if img_obj:
                    st.image(img_obj, use_container_width=True)
                else:
                    st.warning(f"Image not found: {img_rel_path}")

                st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

                # Rating Inputs
                adherence = st.select_slider(
                    "1. Prompt Adherence",
                    options=[1, 2, 3, 4, 5],
                    value=current_scores["adherence"],
                    key=f"slider_adh_{p_key}_{d_label}",
                    help="1 = Completely ignored constraints | 5 = Flawlessly matched all prompt details"
                )

                quality = st.select_slider(
                    "2. Visual Quality",
                    options=[1, 2, 3, 4, 5],
                    value=current_scores["quality"],
                    key=f"slider_qual_{p_key}_{d_label}",
                    help="1 = Glitches, distorted anatomy, blurry | 5 = Flawless commercial studio photorealism"
                )

                authenticity = st.select_slider(
                    "3. Indian Cultural Authenticity",
                    options=[1, 2, 3, 4, 5],
                    value=current_scores["authenticity"],
                    key=f"slider_auth_{p_key}_{d_label}",
                    help="1 = Highly inaccurate or culturally awkward | 5 = Deeply authentic for Indian retail"
                )

                # Save into state
                st.session_state["beta_ratings"][p_key][d_label] = {
                    "adherence": adherence,
                    "quality": quality,
                    "authenticity": authenticity
                }

        st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

        # Bottom navigation buttons
        nav_c1, nav_c2, nav_c3 = st.columns([1, 2, 1])

        with nav_c1:
            if idx > 0:
                if st.button("← Previous Prompt", key="btn_prev_prompt"):
                    st.session_state["beta_prompt_idx"] -= 1
                    st.rerun()

        with nav_c3:
            if idx < 4:
                if st.button("Next Prompt →", key="btn_next_prompt", type="primary"):
                    st.session_state["beta_prompt_idx"] += 1
                    st.rerun()
            else:
                if st.button("SUBMIT EVALUATION ✓", key="btn_submit_eval", type="primary"):
                    save_beta_submission()
                    st.session_state["beta_step"] = "complete"
                    st.rerun()

    # STAGE 3: EVALUATION COMPLETE
    elif st.session_state["beta_step"] == "complete":
        st.markdown(
            """
            <div style="text-align: center; padding: 40px 20px; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; margin: 20px 0;">
                <div style="font-size: 3rem; margin-bottom: 15px;">🎉</div>
                <h2 style="font-size: 1.85rem; font-weight: 800; color: #0F172A; margin-bottom: 10px;">
                    Evaluation Complete!
                </h2>
                <p style="font-size: 1.05rem; color: #334155; margin-bottom: 20px;">
                    Thank you for participating in this sample evaluation prototype.
                </p>
                <div style="max-width: 600px; margin: 0 auto; background: #F8FAFC; border: 1px dashed #CBD5E1; border-radius: 8px; padding: 14px 18px; font-size: 0.85rem; color: #64748B; text-align: left; line-height: 1.55;">
                    ✓ <strong>Data Isolation Verified:</strong> Your 15 image ratings have been securely saved to the prototype beta storage: <code>data/beta_responses/beta_submissions.json</code>.<br>
                    ✓ <strong>Integrity Preserved:</strong> As specified in the architecture, beta prototype submissions do not alter the verified 11-participant assignment survey dataset.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        btn_c1, btn_c2 = st.columns(2)
        with btn_c1:
            if st.button("← Return to Homepage", key="btn_done_home", use_container_width=True):
                st.session_state["beta_step"] = "details"
                st.session_state["view"] = "home"
                st.rerun()
        with btn_c2:
            if st.button("View Assignment Results →", key="btn_done_results", type="primary", use_container_width=True):
                st.session_state["beta_step"] = "details"
                st.session_state["view"] = "assignment_results"
                st.rerun()
