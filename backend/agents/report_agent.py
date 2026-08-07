# Placeholder agent
class ReportAgent:
    def __init__(self):
        self.name = "ReportAgent"

    def process(self, payload):
        return {"status": "ok", "message": "Report agent placeholder", "payload": payload}
