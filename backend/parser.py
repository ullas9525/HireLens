import fitz
import os
import spacy
import re

# Load the English language model from spaCy
# You only need to load this once
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spaCy model 'en_core_web_sm'...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_skills_from_text(text):
    """
    A simple function to extract skills using keywords.
    In a more advanced version, you would use NLP for this.
    """
    # A list of skills relevant to a Data Analyst role
    all_skills = [
        'Python', 'SQL', 'Power BI', 'Tableau', 'Pandas', 'NumPy', 
        'Matplotlib', 'Seaborn', 'Excel', 'Web Scraping', 'EDA',
        'Data Cleaning', 'Statistics', 'MySQL', 'PostgreSQL', 
        'Machine Learning', 'Scikit-learn', 'Git', 'Jupyter', 
        'Data Visualization', 'DAX'
    ]
    
    found_skills = []
    text_lower = text.lower()
    
    for skill in all_skills:
        if skill.lower() in text_lower:
            if skill not in found_skills:
                found_skills.append(skill)
    return found_skills

def parse_resume_advanced(file_path):
    """
    Reads a PDF, extracts text, and uses spaCy to identify key sections.
    """
    try:
        # Part 1: Extract raw text from PDF
        doc = fitz.open(file_path)
        raw_text = ""
        for page in doc:
            raw_text += page.get_text()
        
        # Part 2: Use spaCy for entity and section analysis
        doc = nlp(raw_text)
        
        # Simple extraction logic based on common resume sections
        skills_text = ""
        projects_text = ""
        
        # Find sections and extract content
        # Note: This is a simplified approach and may not work for all resume layouts
        
        text_lower = raw_text.lower()
        
        # Extract skills
        skills_match = re.search(r'skills(.*?)projects|technical skills(.*?)projects|skills(.*?)education', text_lower, re.DOTALL)
        if skills_match:
            skills_text = skills_match.group(1) or skills_match.group(2) or skills_match.group(3)
            
        # Extract projects
        projects_match = re.search(r'projects(.*?)education|projects(.*?)experience|projects(.*?)certifications', text_lower, re.DOTALL)
        if projects_match:
            projects_text = projects_match.group(1) or projects_match.group(2) or projects_match.group(3)

        # Get the list of skills
        skills = extract_skills_from_text(skills_text or raw_text)

        # Get the name of the candidate (simple extraction from the top)
        name = ""
        name_match = re.search(r'([A-Z][a-z]+ [A-Z][a-z]+)', raw_text)
        if name_match:
            name = name_match.group(1)
        
        # Create a structured dictionary
        parsed_data = {
            "name": name,
            "raw_text": raw_text,
            "skills": skills,
            "projects_summary": projects_text.strip(),
        }
        
        return parsed_data
    
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None

if __name__ == "__main__":
    # This block is for testing the function independently
    # This will be called by your orchestrator.py script
    data_folder = os.path.join(os.path.dirname(__file__), "..", "data", "resumes")
    if os.path.exists(data_folder):
        first_file = os.listdir(data_folder)[0]
        file_path = os.path.join(data_folder, first_file)
        
        parsed_resume = parse_resume_advanced(file_path)
        if parsed_resume:
            print(f"Successfully parsed: {first_file}")
            print("\n--- Extracted Data ---")
            print(f"Name: {parsed_resume['name']}")
            print(f"Skills: {parsed_resume['skills']}")
            print(f"Projects Summary: {parsed_resume['projects_summary'][:200]}...")