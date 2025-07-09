# utils/ai_suggestions.py
from utils.cohere_client import co

def generate_ai_suggestions(resume_text, jd_text):
    prompt = (
        f"You are ResumeBot, an AI assistant that gives practical suggestions to improve a resume based on a job description.\n\n"
        f"Resume:\n{resume_text[:1500]}...[truncated]\n\n"
        f"Job Description:\n{jd_text[:1500]}...[truncated]\n\n"
        f"Return 3 to 5 clear, bullet-pointed suggestions to enhance the resume and align better with the job description:"
    )
    
    try:
        response = co.generate(prompt=prompt, model="command", max_tokens=250, temperature=0.7)
        return response.generations[0].text.strip()
    except Exception as e:
        return f"⚠️ Could not generate AI suggestions: {str(e)}"
