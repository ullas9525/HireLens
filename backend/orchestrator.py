import os
import json
from parser import parse_resume_advanced
from analyzer import analyze_resume
from db.database import create_table, insert_result

def get_job_description(jd_path):
    """Reads the job description from the specified file."""
    try:
        with open(jd_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Job description file not found at {jd_path}")
        return None

def main():
    """Runs the full resume analysis workflow."""
    # Step 1: Initialize the database
    create_table()
    
    # Step 2: Load the job description
    jd_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'jds', 'job_description.txt')
    job_description = get_job_description(jd_path)
    if not job_description:
        return

    # Step 3: Parse and analyze all resumes
    resumes_folder = os.path.join(os.path.dirname(__file__), '..', 'data', 'resumes')
    if not os.path.exists(resumes_folder):
        print("Error: Resumes folder not found.")
        return

    for filename in os.listdir(resumes_folder):
        if filename.endswith(".pdf"):
            resume_path = os.path.join(resumes_folder, filename)
            
            # Use the new advanced parser
            parsed_data = parse_resume_advanced(resume_path)
            
            if parsed_data:
                # Use the raw text from the parsed data for analysis
                relevance_score, analysis_summary = analyze_resume(parsed_data['raw_text'], job_description)
                
                # Use the extracted name or fallback to the filename
                candidate_name = parsed_data['name'] if parsed_data['name'] else filename
                
                # Step 4: Insert results into the database
                insert_result(candidate_name, relevance_score, analysis_summary, json.dumps(parsed_data['skills']))
                print(f"Analysis for {candidate_name}: Score {relevance_score:.2f}%. Results saved to database.")

if __name__ == "__main__":
    main()