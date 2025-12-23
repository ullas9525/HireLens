from celery import Celery
import os
import json
import sqlite3

# Import your existing functions as tasks
from parser import parse_resume_advanced
from analyzer import analyze_resume
from db.database import create_table, insert_result

# Configure Celery
app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@app.task
def process_resume_task(file_path, job_description_text):
    """
    This is the main asynchronous task that processes a single resume.
    """
    try:
        # Step 1: Parse the resume
        parsed_data = parse_resume_advanced(file_path)
        
        if not parsed_data:
            print(f"Failed to parse resume at {file_path}")
            return

        # Step 2: Analyze the parsed resume
        relevance_score, analysis_summary = analyze_resume(parsed_data['raw_text'], job_description_text)
        
        # Step 3: Insert the results into the database
        # Use the extracted name or fallback to the filename
        candidate_name = parsed_data['name'] if parsed_data['name'] else os.path.basename(file_path)
        
        # Ensure the database table exists
        create_table()
        
        # Save the results
        insert_result(candidate_name, relevance_score, analysis_summary, json.dumps(parsed_data['skills']))
        
        print(f"SUCCESS: Analysis for {candidate_name} completed and saved. Score: {relevance_score:.2f}%")
        
    except Exception as e:
        print(f"FAILURE: An error occurred while processing {file_path}: {e}")

if __name__ == '__main__':
    # This block is for running the Celery worker from the terminal
    print("Celery worker is running...")