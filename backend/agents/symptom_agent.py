# Placeholder agent
class SymptomAgent:
    def __init__(self):
        self.name = "SymptomAgent"

    def process(self, payload):
        return {"status": "ok", "message": "Symptom agent placeholder", "payload": payload}
