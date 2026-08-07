from services.gemini_service import gemini
from utils.file_loader import load_prompt


class KnowledgeAgent:

    def __init__(self):

        self.prompt = load_prompt(
            "knowledge_prompt.txt"
        )

    def search(self, query):

        prompt = self.prompt.replace(
            "{query}",
            query
        )

        return gemini.generate_json(prompt)


knowledge_agent = KnowledgeAgent()
