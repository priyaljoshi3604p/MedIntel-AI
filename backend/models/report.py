from dataclasses import dataclass

@dataclass
class Report:
    patient_id: str = ""
    summary: str = ""
    findings: str = ""
    recommendations: str = ""
