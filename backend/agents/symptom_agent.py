from services.gemini_service import gemini
from utils.file_loader import load_prompt


class SymptomAgent:

    def __init__(self):
        self.prompt = load_prompt("symptom_prompt.txt")

    def analyze(self, symptoms):

        symptom_text = "\n".join(symptoms)

        prompt = self.prompt.replace(
            "{symptoms}",
            symptom_text
        )

        result = gemini.generate_json(prompt)

        return result


symptom_agent = SymptomAgent()