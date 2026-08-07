from fastapi import APIRouter
from pydantic import BaseModel

from agents.knowledge_agent import knowledge_agent

router = APIRouter()


class KnowledgeRequest(BaseModel):

    query: str


@router.post("/knowledge")
def medical_search(data: KnowledgeRequest):

    result = knowledge_agent.search(
        data.query
    )

    return result