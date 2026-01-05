# AI Resume Screening Tool

## Overview
This project is a beginner-friendly AI-assisted resume screening tool that analyzes
how well a resume matches a given job description. It automates the initial resume
shortlisting process using keyword matching and relevance scoring.

The application is deployed as a web app using Streamlit.

## Features
- Accepts resume text and job description text as input
- Cleans and processes text data
- Identifies matched and missing skills
- Calculates a resume–job match percentage
- Provides a recommendation based on the match score
- Deployed as an interactive web application

## Tech Stack
- Python
- Streamlit
- GitHub
- Rule-based text analysis (AI-assisted automation)

## How It Works
1. User pastes resume text
2. User pastes job description text
3. The system extracts keywords from both inputs
4. Matching skills are identified
5. A match score is calculated and displayed
6. Missing skills and recommendations are shown

## How to Run Locally
```bash
pip install streamlit
streamlit run app.py

Live Demo

Access the deployed application here:
👉 ## Live Demo
👉 (https://resumescreeningtool-ssahs5dodvfkotfacucqva.streamlit.app/)


Future Enhancements

PDF resume support

Advanced NLP-based matching

Skill weighting and ranking

Database integration for multiple resumes
