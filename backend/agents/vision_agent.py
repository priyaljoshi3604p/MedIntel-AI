from PIL import Image
from services.gemini_service import gemini
from utils.file_loader import load_prompt


class VisionAgent:

    def __init__(self):
        self.prompt = load_prompt("vision_prompt.txt")

    def analyze(self, image_path):

    try:

        image = Image.open(image_path)

        response = gemini.model.generate_content(
            [
                self.prompt,
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


vision_agent = VisionAgent()