from sentence_transformers import SentenceTransformer, util
import re

# Load a pre-trained model for generating embeddings.
# This model converts sentences and paragraphs into a numerical vector.
try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
except Exception as e:
    print(f"Error loading model: {e}")
    print("Trying to download the model...")
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
def analyze_resume_semantic(resume_text, job_description):
    """
    Analyzes resume text against a job description using semantic similarity.
    """
    try:
        # Convert both texts to lowercase for consistent analysis
        resume_text_lower = resume_text.lower()
        job_description_lower = job_description.lower()
        
        # Combine texts to create a more comprehensive comparison
        combined_text = f"{resume_text_lower} {job_description_lower}"

        # Generate vector embeddings for both texts
        resume_embedding = model.encode(resume_text_lower, convert_to_tensor=True)
        jd_embedding = model.encode(job_description_lower, convert_to_tensor=True)

        # Calculate cosine similarity between the embeddings
        # Cosine similarity measures the angle between two vectors, ranging from -1 to 1.
        cosine_score = util.cos_sim(resume_embedding, jd_embedding).item()

        # Scale the score to be from 0-100 for easier interpretation
        relevance_score = (cosine_score + 1) / 2 * 100
        
        analysis_summary = f"Semantic similarity score based on vector embeddings."

        return relevance_score, analysis_summary

    except Exception as e:
        print(f"Error during semantic analysis: {e}")
        return 0, "Error during analysis."

# This is the main function that will be called by the orchestrator
def analyze_resume(resume_text, job_description):
    return analyze_resume_semantic(resume_text, job_description)

if __name__ == "__main__":
    # Test block for semantic analysis
    sample_resume = "Data Analyst with skills in Python, SQL, and Power BI. Experience in web scraping."
    sample_jd = "Seeking a Data Scientist proficient in Python, SQL, and data visualization. Knowledge of web scraping is a plus."
    
    score, summary = analyze_resume_semantic(sample_resume, sample_jd)
    print(f"Sample Score: {score:.2f}%")
    print(f"Summary: {summary}")