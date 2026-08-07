from services.gemini_service import gemini


class VitalsAgent:

    def analyze(self, vitals):

        prompt = f"""
You are an Emergency Medicine AI.

Analyze the patient's vital signs.

Vitals:
{vitals}

Return ONLY valid JSON.

{{
    "severity":"",
    "risk_score":0,
    "abnormal_parameters":[],
    "possible_conditions":[],
    "recommended_action":"",
    "triage_priority":"Green | Yellow | Orange | Red"
}}
"""

        return gemini.generate_json(prompt)


vitals_agent = VitalsAgent()