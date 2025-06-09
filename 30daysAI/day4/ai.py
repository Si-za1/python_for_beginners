#this is where we will handle prompt and openai stuffs 
from openai import OpenAI


def calm_bot_message (error_type, error_msg, tb):
    client = OpenAI(api_key="yourkey")

    prompt = f"""
    You are CalmBot, a calm and helpful AI that helps developers understand and fix errors.

    Error Type: {error_type}
    Message: {error_msg}
    Traceback:
    {tb}

    CalmBot says:
    - Explain what went wrong in beginner-friendly terms.
    - Motivate the user.
    - Offer one or two actionable suggestions to fix it.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            max_tokens=1000,
            temperature=0.6,
            messages=[
                {"role": "system", "content": "You are a calm, friendly AI who helps programmers fix errors with kindness."},
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❗ CalmBot couldn't process the error: {str(e)}"
