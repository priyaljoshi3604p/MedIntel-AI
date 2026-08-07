from fastapi import FastAPI

from api.upload import router as upload_router
from api.analyze import router as analyze_router
from api.reports import router as reports_router
from api.health import router as health_router

app = FastAPI(
    title="MedIntel AI",
    version="1.0.0"
)

app.include_router(upload_router)
app.include_router(analyze_router)
app.include_router(reports_router)
app.include_router(health_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to MedIntel AI Backend!"
    }