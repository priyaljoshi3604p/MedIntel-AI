from fastapi import FastAPI

from api.symptom_api import router as symptom_router
from api.vision_api import router as vision_router
from api.report_api import router as report_router
from api.vitals_api import router as vitals_router
from api.knowledge_api import router as knowledge_router
from api.decision_api import router as decision_router
from api.explanation_api import router as explanation_router

app = FastAPI(
    title="Enterprise Multimodal Clinical Intelligence Platform",
    version="1.0.0"
)

app.include_router(symptom_router)
app.include_router(vision_router)
app.include_router(report_router)
app.include_router(vitals_router)
app.include_router(knowledge_router)
app.include_router(decision_router)
app.include_router(explanation_router)


@app.get("/")
def home():

    return {
        "project": "Enterprise Multimodal Clinical Intelligence Platform",
        "version": "1.0.0",
        "status": "Running"
    }