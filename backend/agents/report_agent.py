from services.pdf_service import pdf_service
from services.gemini_service import gemini
from utils.file_loader import load_prompt


class ReportAgent:

    def __init__(self):

        self.prompt = load_prompt("diagnosis_prompt.txt")

    def analyze(self, pdf_path):

        try:

            report = pdf_service.extract_text(pdf_path)

            prompt = self.prompt.replace(
                "{patient_data}",
                report
            )

            result = gemini.generate_json(prompt)

            return result

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }


report_agent = ReportAgent()