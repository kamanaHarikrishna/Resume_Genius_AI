import cohere
import os

from utils.cohere_client import co


def recommend_skills(resume_text, jd_text):
    prompt = f"Compare this resume with the job description and list key missing skills.\n\nResume:\n{resume_text}\n\nJob Description:\n{jd_text}"
    response = co.generate(prompt=prompt, model="command", max_tokens=150)
    return response.generations[0].text.strip().split("\n")