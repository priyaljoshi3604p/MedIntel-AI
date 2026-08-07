from fastapi import APIRouter
from pydantic import BaseModel
from agents.symptom_agent import symptom_agent

router = APIRouter()


class SymptomRequest(BaseModel):

    symptoms: list[str]


@router.post("/symptoms")

def analyze_symptoms(data: SymptomRequest):

    result = symptom_agent.analyze(data.symptoms)

    return result