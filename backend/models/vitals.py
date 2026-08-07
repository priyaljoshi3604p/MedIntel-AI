from dataclasses import dataclass

@dataclass
class Vitals:
    temperature: float = 0.0
    heart_rate: int = 0
    blood_pressure: str = ""
    oxygen_saturation: float = 0.0
