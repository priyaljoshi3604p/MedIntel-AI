from fastapi import APIRouter
from pydantic import BaseModel

from agents.vitals_agent import vitals_agent

router = APIRouter()


class VitalsRequest(BaseModel):

    heart_rate: int
    blood_pressure: str
    oxygen_saturation: int
    temperature: float
    respiratory_rate: int


@router.post("/vitals")
def analyze_vitals(data: VitalsRequest):

    result = vitals_agent.analyze(
        data.model_dump()
    )

    return result