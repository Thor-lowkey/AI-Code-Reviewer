import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def review_code(user_code: str) -> str:
    system_prompt = (
        "You are a Senior Software Engineer and Code Reviewer with expertise in Python, C++, Java, JavaScript, and software engineering best practices.\n\n"
        "Analyze the code provided below and perform a professional code review.\n\n"
        "For your review, provide:\n"
        "1. Code Summary\n"
        "   - Briefly explain what the code does.\n"
        "2. Bugs and Errors\n"
        "   - Identify any logical bugs, syntax issues, runtime errors, or potential crashes.\n"
        "3. Code Quality\n"
        "   - Identify poor naming, duplicate code, unnecessary complexity, or bad practices.\n"
        "4. Performance\n"
        "   - Point out inefficient algorithms or operations.\n"
        "5. Security Issues\n"
        "   - Identify any security risks such as unsafe input handling, hardcoded credentials, etc.\n"
        "6. Formatting and Style\n"
        "   - Check readability, indentation, comments, and adherence to coding standards.\n"
        "7. Suggested Fixes\n"
        "   - Provide concise recommendations for improving the code.\n"
        "8. Overall Score\n"
        "   - Give a code quality score out of 100.\n\n"
        "Rules:\n"
        "- Be constructive and beginner-friendly.\n"
        "- Do not rewrite the entire program unless necessary.\n"
        "- Focus on practical improvements.\n"
        "- If no issues are found, explicitly state that the code is well-written.\n"
        "- Use clear markdown bullet points."
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_code,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.2,
            ),
        )
        return response.text
    except Exception as e:
        return f"Error connecting to Gemini API: {str(e)}"


if __name__ == "__main__":
    sample_code = """
def calculate_area(r):
    password = "admin_secret_123"
    pi = 3.14
    return pi * r * r
"""

    print("Testing your custom Code Review prompt layout...")
    result = review_code(sample_code)
    print("\n" + result)