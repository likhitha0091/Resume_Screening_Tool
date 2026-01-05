import streamlit as st
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text.split()

def analyze_resume(resume_text, job_description):
    resume_words = set(clean_text(resume_text))
    job_words = set(clean_text(job_description))

    matched_skills = resume_words.intersection(job_words)
    missing_skills = job_words - resume_words

    match_score = (len(matched_skills) / len(job_words)) * 100 if job_words else 0

    if match_score >= 70:
        recommendation = "Good match for the role."
    else:
        recommendation = "Improve missing skills to increase job match."

    return round(match_score, 2), matched_skills, missing_skills, recommendation


st.set_page_config(page_title="Resume Screening Tool")

st.title("AI Resume Screening Tool")
st.write("Paste your resume and job description to analyze the match.")

resume_text = st.text_area("Paste Resume Text")
job_description = st.text_area("Paste Job Description Text")

if st.button("Analyze"):
    if resume_text and job_description:
        score, matched, missing, recommendation = analyze_resume(resume_text, job_description)

        st.subheader("Results")
        st.write(f"**Match Score:** {score}%")

        st.write("**Matched Skills:**")
        st.write(", ".join(sorted(matched)) if matched else "None")

        st.write("**Missing Skills:**")
        st.write(", ".join(sorted(missing)) if missing else "None")

        st.success(recommendation)
    else:
        st.warning("Please paste both resume and job description.")
