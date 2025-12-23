# HireLens
🎯 HireLens: AI-Powered Resume Evaluator

A professional Streamlit application that leverages AI + semantic analysis to evaluate resumes against job descriptions, helping recruiters save time, reduce bias, and identify the best candidates faster.

✨ Features

🤖 AI-Powered Matching – Uses sentence-transformers to compute semantic similarity between resumes & job descriptions

📄 Smart Resume Parsing – Extracts text, detects candidate names, and identifies key skills from PDFs

📝 Job Description Processing – Upload JD files or paste text directly for instant processing

📊 Candidate Ranking – Automatically scores & ranks resumes by relevance

🔎 Skills Gap Analysis – Highlights missing skills & generates match-level assessments

📥 Export Results – Download ranked results as CSV or PDF reports

💬 AI Assistant – Built-in chatbot powered by Google Gemini for recruitment insights

🎨 Modern UI – Sleek black & white theme, responsive design, and professional dashboard layout

⚡ Installation

1️⃣ Clone the Repository

git clone <repository-url>
cd hirelens


2️⃣ Install Dependencies
pip install streamlit sentence-transformers spacy pandas PyMuPDF requests hashlib fpdf


3️⃣ Download spaCy Model
python -m spacy download en_core_web_sm

🚀 Usage

Run the App

streamlit run app.py


Open your browser at http://localhost:8501

Upload a Job Description (PDF or paste text)

Upload Candidate Resumes (PDF format)

Click Start Analysis to begin evaluation

View:

🏆 Top Performer Highlight

📑 Detailed Candidate Rankings

🛠️ Skill Gap Analysis

⚙️ Configuration

🔑 API Key – Update API_KEY with your Google Gemini API key for chatbot functionality

💾 Database – Results stored in data/results.db (auto-created)

📂 Resume Storage – Option to permanently save uploaded resumes (toggle in sidebar)

🛠 Tech Stack
Layer	Technology
Frontend	Streamlit + Custom CSS (Black/White Theme)
Backend	Python + SQLite
AI/NLP	Sentence Transformers, spaCy
PDF Parsing	PyMuPDF (fitz)
APIs	Google Gemini

🗄 Database Schema
analysis_results Table
Column	Description
id	Primary key
resume_name	Candidate file name
relevance_score	AI-computed similarity score
analysis_summary	Text summary of match
extracted_skills	Parsed skills from resume
match_level	High / Medium / Low
skill_gaps	Missing skills
file_hash	Hash to prevent duplicate entries

📜 License
Licensed under the MIT License.

