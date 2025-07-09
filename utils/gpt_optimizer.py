import cohere
import os
from utils.cohere_client import co

MAX_PROMPT_TOKENS = 4000  # Staying under Cohere's 4081 token limit
TRUNCATED_RESUME_LEN = 2500
TRUNCATED_JD_LEN = 1000

def truncate_text(text, max_length):
    return text[:max_length] if len(text) > max_length else text

def optimize_resume(resume_text, jd_text, tone="Professional"):
    # Truncate inputs to stay within token limits
    resume_text = truncate_text(resume_text, TRUNCATED_RESUME_LEN)
    jd_text = truncate_text(jd_text, TRUNCATED_JD_LEN)

    prompt = (
        f"Rewrite the following resume content to better align with this job description. "
        f"Use a {tone} tone.\n\nResume:\n{resume_text}\n\nJob Description:\n{jd_text}"
    )

    response = co.generate(
        prompt=prompt,
        model="command",  # Use a valid Cohere model
        max_tokens=800
    )
    return response.generations[0].text.strip()

def rewrite_by_persona(optimized_text, persona):
    optimized_text = truncate_text(optimized_text, 3000)  # Optional: extra safety

    persona_prompt = (
        f"Rewrite the following resume content to match the persona of a {persona}. "
        f"Keep it concise, role-specific, and high-impact:\n\n{optimized_text}"
    )

    response = co.generate(
        prompt=persona_prompt,
        model="command",
        max_tokens=600
    )
    return response.generations[0].text.strip()
