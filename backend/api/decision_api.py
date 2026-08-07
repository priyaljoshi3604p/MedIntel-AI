from fastapi import APIRouter
from pydantic import BaseModel

from agents.decision_agent import decision_agent

router = APIRouter()


class DecisionRequest(BaseModel):

    symptom_result: dict

    vision_result: dict

    report_result: dict

    vitals_result: dict

    knowledge_result: dict


@router.post("/decision")

def decision(data: DecisionRequest):

    result = decision_agent.decide(

        data.symptom_result,

        data.vision_result,

        data.report_result,

        data.vitals_result,

        data.knowledge_result

    )

    return result
