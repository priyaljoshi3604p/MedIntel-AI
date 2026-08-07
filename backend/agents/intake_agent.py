from typing import Dict
import json


class IntakeAgent:

    def __init__(self):
        self.name = "IntakeAgent"

    def process(self, payload: Dict):

        patient = {
            "patient_id": payload.get("patient_id", ""),
            "name": payload.get("name", ""),
            "age": payload.get("age", ""),
            "gender": payload.get("gender", ""),

            "symptoms": payload.get("symptoms", []),

            "medical_history": payload.get("medical_history", []),

            "current_medications": payload.get("current_medications", []),

            "allergies": payload.get("allergies", []),

            "vitals": payload.get("vitals", {}),

            "uploaded_image": payload.get("uploaded_image"),

            "uploaded_report": payload.get("uploaded_report"),

            "speech_transcript": payload.get("speech_transcript", "")
        }

        return {
            "success": True,
            "patient": patient
        }


intake_agent = IntakeAgent()
