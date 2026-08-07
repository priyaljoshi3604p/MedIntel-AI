import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY is None:
    raise Exception("GEMINI_API_KEY not found in .env")

genai.configure(api_key=API_KEY)

MODEL = genai.GenerativeModel(
    model_name="gemini-2.5-flash"
)


class GeminiService:

    def __init__(self):
        self.model = MODEL

    def generate(self, prompt: str):

        try:

            response = self.model.generate_content(prompt)

            return {
                "success": True,
                "response": response.text
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    def generate_json(self, prompt: str):

        system_prompt = f"""
Return ONLY valid JSON.

{prompt}
"""

        try:

            response = self.model.generate_content(system_prompt)

            text = response.text.strip()

            if text.startswith("```json"):
                text = text.replace("```json", "")
                text = text.replace("```", "")
                text = text.strip()

            data = json.loads(text)

            return {
                "success": True,
                "response": data
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    def analyze_image(self, image, prompt):

        try:

            response = self.model.generate_content(
                [
                    prompt,
                    image
                ]
            )

            return {
                "success": True,
                "response": response.text
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    def chat(self, history, message):

        messages = history.copy()

        messages.append(message)

        try:

            chat = self.model.start_chat()

            for msg in messages[:-1]:
                chat.send_message(msg)

            response = chat.send_message(messages[-1])

            return {
                "success": True,
                "response": response.text
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }


gemini = GeminiService()
