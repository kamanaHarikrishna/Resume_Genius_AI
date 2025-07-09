import textstat

def audit_resume_sections(resume_text):
    resume_lower = resume_text.lower()

    # Section audit
    section_feedback = {
        "Objective": "Present" if "objective" in resume_lower else "Needs Improvement",
        "Experience": "Present" if "experience" in resume_lower else "Needs Improvement",
        "Education": "Present" if "education" in resume_lower else "Needs Improvement",
        "Skills": "Present" if "skills" in resume_lower else "Needs Improvement",
    }

    # Readability metrics (optional)
    section_feedback.update({
        "readability Score": round(textstat.flesch_reading_ease(resume_text), 2),
        "sentence Count": textstat.sentence_count(resume_text),
        "word Count": textstat.lexicon_count(resume_text),
        "estimated Reading Time (mins)": round(textstat.reading_time(resume_text), 2)
    })

    return section_feedback
