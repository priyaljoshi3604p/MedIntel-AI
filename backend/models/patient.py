
class Patient(BaseModel):

    patient_id: str

    name: str

    age: int

    gender: str

    symptoms: List[str]

    medical_history: List[str]

    current_medications: List[str]

    allergies: List[str]

    vitals: Dict

    speech_transcript: str = ""