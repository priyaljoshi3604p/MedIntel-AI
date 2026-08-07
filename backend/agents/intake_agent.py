# Placeholder agent
class IntakeAgent:
    def __init__(self):
        self.name = "IntakeAgent"

    def process(self, payload):
        return {"status": "ok", "message": "Intake agent placeholder", "payload": payload}
