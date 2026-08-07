from fastapi import APIRouter
from pydantic import BaseModel

from agents.explanation_agent import explanation_agent

router = APIRouter()


class ExplanationRequest(BaseModel):

    decision_result: dict


@router.post("/explanation")
def explain(data: ExplanationRequest):

    return explanation_agent.explain(
        data.decision_result
    )
