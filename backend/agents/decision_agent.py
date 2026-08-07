# Placeholder agent
class DecisionAgent:
    def __init__(self):
        self.name = "DecisionAgent"

    def process(self, payload):
        return {"status": "ok", "message": "Decision agent placeholder", "payload": payload}
