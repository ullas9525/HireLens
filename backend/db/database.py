import sqlite3

DATABASE_PATH = 'data/results.db'

def create_table():
    """Creates the analysis_results table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analysis_results (
            id INTEGER PRIMARY KEY,
            resume_name TEXT NOT NULL,
            relevance_score REAL NOT NULL,
            analysis_summary TEXT,
            extracted_skills TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_result(resume_name, relevance_score, analysis_summary, extracted_skills):
    """Inserts a new analysis result into the table."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO analysis_results (resume_name, relevance_score, analysis_summary, extracted_skills)
        VALUES (?, ?, ?, ?)
    ''', (resume_name, relevance_score, analysis_summary, extracted_skills))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
    print("Database and table created successfully.")