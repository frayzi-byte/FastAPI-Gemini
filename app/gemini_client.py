from dotenv import dotenv_values
from google import genai

config = dotenv_values(".env")

client = genai.Client(api_key=config["GEMINI_KEY"])

def get_answer_from_gemini(promt : str):
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite", contents=promt
    )
    return response.text

if (__name__ == "__main__"):
    get_answer_from_gemini()