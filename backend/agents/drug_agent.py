# Placeholder agent
class DrugAgent:
    def __init__(self):
        self.name = "DrugAgent"

    def process(self, payload):
        return {"status": "ok", "message": "Drug agent placeholder", "payload": payload}
