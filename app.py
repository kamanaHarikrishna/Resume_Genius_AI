# resume-genius-ai/app.py
import streamlit as st
import plotly.graph_objects as go
import base64
import pandas as pd
import matplotlib.pyplot as plt
import textstat


# Page configuration
st.set_page_config(page_title="Resume Genius AI", layout="wide")


# Utility imports
from utils.ai_suggestions import generate_ai_suggestions
from utils.resume_parser import extract_resume_text
from utils.jd_parser import extract_jd_text
from utils.ats_matcher import calculate_ats_score
from utils.gpt_optimizer import optimize_resume, rewrite_by_persona
from utils.cover_letter_gen import generate_cover_letter
from utils.persona_handler import get_persona_options
from utils.job_role_detector import detect_job_role
from utils.resume_auditor import audit_resume_sections
from utils.multi_jd_scorer import score_multiple_jds
from utils.ats_friendly_checker import check_ats_friendly
from utils.job_scorer import calculate_job_readiness
from utils.skill_recommender import recommend_skills
from utils.career_chatbot import launch_career_chatbot
from utils.keyword_cloud import generate_missing_keywords_cloud


# Load and encode background image in base64
@st.cache_data
def get_base64_background(image_path):
    try:
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        return encoded
    except FileNotFoundError:
        return None

background_img = get_base64_background("bg.jpg")

if background_img:
    st.markdown(f"""
        <style>
        html, body {{
            height: 100%;
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
        }}

        body::before {{
            content: "";
            background-image: url("data:image/jpg;base64,{background_img}") !important;
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            z-index: -1;
            opacity: 0.6;
        }}

        [data-testid="stAppViewContainer"] {{
            background-color: rgba(255, 255, 255, 0.92);
            padding: 2rem;
            border-radius: 15px;
            max-width: 95%;
            margin: auto;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}

        h1, h2, h3 {{
            color: #1c1c1c;
            font-weight: 700;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.4);
        }}
        </style>
    """, unsafe_allow_html=True)
else:
    st.warning("⚠️ Background image not found. Please make sure 'bg.jpg' exists in your project folder.")


# Title
st.title("\U0001F4C4 Resume Genius AI - Optimize Your Resume with AI")

# Sidebar inputs
st.sidebar.header("Upload & Options")
dark_mode = st.sidebar.checkbox("\U0001F319 Enable Dark Mode")
if dark_mode:
    st.markdown("""
        <style>
        html, body {
            background-color: #121212;
            color: #e0e0e0;
        }
        [data-testid="stAppViewContainer"] {
            background-color: rgba(33, 33, 33, 0.95);
            color: #e0e0e0;
        }
        h1, h2, h3 {
            color: #ffffff;
        }
        .stTextInput > div > div > input,
        .stTextArea > div > textarea {
            background-color: #2c2c2c;
            color: #ffffff;
            border: 1px solid #555;
        }
        .stButton > button {
            background-color: #bb86fc;
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)

resume_file = st.sidebar.file_uploader("Upload your Resume (PDF/DOCX)", type=["pdf", "docx"])
job_descriptions = st.sidebar.text_area("Paste up to 3 Job Descriptions (separate by '###')")
persona = st.sidebar.selectbox("Choose Persona", get_persona_options())
experience_level = st.sidebar.selectbox("Years of Experience", ["0-2 years", "3-5 years", "6-10 years", "10+ years"])
tone_map = {
    "0-2 years": "Basic",
    "3-5 years": "Intermediate",
    "6-10 years": "Advanced",
    "10+ years": "Executive"
}
tone = tone_map[experience_level]

run_opt = st.sidebar.button("Run Optimization")

# Main processing
if run_opt and resume_file and job_descriptions:
    st.success("Processing your resume...")
    resume_text = extract_resume_text(resume_file)
    jd_list = extract_jd_text(job_descriptions)

    ats_results = score_multiple_jds(resume_text, jd_list)
    st.subheader("\U0001F4CA ATS Match Scores")
    st.dataframe(ats_results)

    optimized_resume = optimize_resume(resume_text, jd_list[0], tone)
    persona_resume = rewrite_by_persona(optimized_resume, persona)
    st.subheader("\u270D\ufe0f Optimized Resume Content")
    st.text_area("Enhanced Resume", persona_resume, height=400)
    st.download_button("\U0001F4C4 Download Optimized Resume", data=persona_resume, file_name="Optimized_Resume.txt", mime="text/plain")
    
    st.subheader("🤖 AI Suggestions Panel")
    with st.spinner("Analyzing resume and job description..."):
        ai_feedback = generate_ai_suggestions(resume_text, jd_list[0])
        if "⚠️" in ai_feedback:
            st.warning(ai_feedback)
        else:
            st.markdown(f"<div style='background-color:#f9f9f9; padding:1rem; border-radius:8px;'>{ai_feedback}</div>", unsafe_allow_html=True)

    st.subheader("\U0001F4DD AI-Generated Cover Letter")
    cover_letter_text = generate_cover_letter(persona_resume, jd_list[0])
    st.text_area("Cover Letter", cover_letter_text, height=300)
    st.download_button("\U0001F4DD Download Cover Letter", data=cover_letter_text, file_name="Cover_Letter.txt", mime="text/plain")

    

    if resume_file:
     resume_text = extract_resume_text(resume_file)

    st.subheader("🔍 Resume Section Audit")
    audit_results = audit_resume_sections(resume_text)

    section_status = []
    metrics = []

    for section, status in audit_results.items():
        if isinstance(status, str):
            if status == "Present":
                section_status.append(f"✔️ {section}: Present")
            elif status == "Needs Improvement":
                section_status.append(f"⚠️ {section}: Needs Improvement")
            else:
                section_status.append(f"❌ {section}: Missing")
        else:
            metrics.append(f"📌 {section}: {status}")

    st.markdown("**Section Status:**")
    st.markdown("\n".join(section_status))

    st.markdown("**Readability Metrics:**")
    st.markdown("\n".join(metrics))

    st.subheader("\U0001F6E1\ufe0f ATS-Friendliness Check")
    st.json(check_ats_friendly(resume_file))



    st.subheader("\U0001F4C8 Skill Gap Recommendations")
    recommended_skills = recommend_skills(resume_text, jd_list[0])
    if isinstance(recommended_skills, list):
     st.markdown("#### Recommended Skills Based on Job Description:")
     st.markdown("\n".join([f"- {item}" for item in recommended_skills if item.strip() != ""]))
    else:
     st.write(recommended_skills)
     
    st.subheader("\U0001F9E0 Missing Keywords Word Cloud")
    img = generate_missing_keywords_cloud(resume_text, jd_list[0])
    st.image(img)

    st.subheader("\U0001F3AF Job-Readiness Score")
    score = calculate_job_readiness(ats_results, audit_resume_sections(resume_text))

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Resume Job-Readiness Score", 'font': {'size': 24}},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#0072f5"},
            'steps': [
                {'range': [0, 50], 'color': "#ffcccc"},
                {'range': [50, 75], 'color': "#fff3cd"},
                {'range': [75, 100], 'color': "#d4edda"}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': score
            }
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

    # Career Chatbot (always active if resume is uploaded)
if resume_file and job_descriptions:
    resume_text = extract_resume_text(resume_file)
    st.subheader("\U0001F4AC Ask CareerGPT")
    user_input = st.text_input("Ask any career or resume question:")
    if user_input:
        try:
            st.write(launch_career_chatbot(user_input, resume_text))
        except Exception as e:
            st.error(f"CareerGPT Error: {str(e)}")


# Footer
st.markdown("""
    <hr style="margin-top: 50px;">
    <div style='text-align: center; color: gray; font-size: 0.9rem;'>
        ✨ Developed with ❤️ by <strong>Hari Krishna</strong>
    </div>
""", unsafe_allow_html=True)
