import cohere
from utils.cohere_client import co

def launch_career_chatbot(user_input, resume_context):
    """
    Launches a career advice chatbot using Cohere's language model.

    Parameters:
    - user_input: str - The user's question about resume/career.
    - resume_context: str - Parsed resume text.

    Returns:
    - str - AI-generated response or error message.
    """

    # Ensure token-safe prompt length (Cohere limit is ~4096 tokens incl. prompt + response)
    if len(resume_context) > 1500:
        resume_context = resume_context[:1500] + "\n...[truncated]"

    if not user_input.strip():
        return "❗ Please enter a question."

    prompt = (
        "You are CareerGPT, an expert AI assistant for resumes, job applications, and career guidance.\n\n"
        "Here is the user's resume summary:\n"
        f"{resume_context}\n\n"
        "Here is the user's question:\n"
        f"{user_input}\n\n"
        "Please respond with practical, clear, and friendly advice."
    )

    try:
        response = co.generate(
            prompt=prompt,
            model="command",
            max_tokens=350,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except cohere.error.CohereError as ce:
        return f"⚠️ CareerGPT Cohere Error: {str(ce)}"
    except Exception as e:
        return f"⚠️ An unexpected error occurred: {str(e)}"

