import cohere
import os

from utils.cohere_client import co


def detect_job_role(resume_text):
    prompt = f"Based on this resume, suggest the most suitable job roles.\n\n{resume_text}"
    response = co.generate(prompt=prompt, model="command", max_tokens=100)
    return response.generations[0].text.strip()