import cohere
import os

from utils.cohere_client import co
def generate_cover_letter(resume_text, jd_text):
    prompt = f"Generate a personalized cover letter based on this resume and job description.\n\nResume:\n{resume_text}\n\nJob Description:\n{jd_text}"
    response = co.generate(prompt=prompt, model="command", max_tokens=600)
    return response.generations[0].text.strip()