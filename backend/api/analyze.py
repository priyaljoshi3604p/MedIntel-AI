from fastapi import APIRouter
from pydantic import BaseModel

from services.gemini_service import ask_gemini

router = APIRouter()


class AnalyzeRequest(BaseModel):
    prompt: str


@router.post("/analyze")
def analyze(request: AnalyzeRequest):
    result = ask_gemini(request.prompt)

    return {
        "success": True,
        "response": result
    }