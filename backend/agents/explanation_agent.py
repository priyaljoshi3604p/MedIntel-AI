from services.gemini_service import gemini
from utils.file_loader import load_prompt


class ExplanationAgent:

    def __init__(self):
        self.prompt = load_prompt("explanation_prompt.txt")

    def explain(self, decision_result):

        prompt = self.prompt.replace(
            "{patient_data}",
            str(decision_result)
        )

        result = gemini.generate_json(prompt)

        return result


explanation_agent = ExplanationAgent()
