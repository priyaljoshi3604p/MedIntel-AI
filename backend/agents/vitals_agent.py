# Placeholder agent
class VitalsAgent:
    def __init__(self):
        self.name = "VitalsAgent"

    def process(self, payload):
        return {"status": "ok", "message": "Vitals agent placeholder", "payload": payload}
