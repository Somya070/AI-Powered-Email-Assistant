from gemini_api import generate_content

def is_important_email(subject, body):
    """
    Decide whether the email is important: job, urgent, meeting, or personal.
    Returns True or False.
    """
    prompt = f"""
    Decide whether the following email is important (urgent, job-related, meeting-related, or personal).

    Subject: {subject}
    Body: {body}

    Reply with "yes" or "no" only.
    """
    try:
        response = generate_content(prompt)
        answer = response.strip().lower()
        return "yes" in answer
    except Exception as e:
        print("Gemini Error:", e)
        return False

def summarize_email(subject, body):
    """
    Summarize the email in 1–2 sentences.
    """
    prompt = f"""
    Summarize the following email in 1-2 concise sentences.

    Subject: {subject}
    Body: {body}
    """
    try:
        return generate_content(prompt).strip()
    except Exception as e:
        print("Gemini Summary Error:", e)
        return "Summary not available."
