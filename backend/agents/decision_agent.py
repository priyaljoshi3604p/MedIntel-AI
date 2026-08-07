from services.gemini_service import gemini
from utils.file_loader import load_prompt


class DecisionAgent:

    def __init__(self):

        self.prompt = load_prompt(
            "triage_prompt.txt"
        )

    def decide(
        self,
        symptom_result,
        vision_result,
        report_result,
        vitals_result,
        knowledge_result
    ):

        patient_data = f"""

You are the Chief Emergency Physician.

Five specialist AI agents have independently analyzed the patient.

Your job is to combine all findings.

If agents disagree,
explain why.

Never ignore any evidence.

Produce the safest clinical decision.

==================================================

SYMPTOM AGENT

{symptom_result}

==================================================

VISION AGENT

{vision_result}

==================================================

REPORT AGENT

{report_result}

==================================================

VITALS AGENT

{vitals_result}

==================================================

KNOWLEDGE AGENT

{knowledge_result}

==================================================

"""



        prompt = self.prompt.replace(
            "{patient_data}",
            patient_data
        )

        result = gemini.generate_json(prompt)

        return result


decision_agent = DecisionAgent()