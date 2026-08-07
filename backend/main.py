from fastapi import FastAPI

app = FastAPI(title="MedIntel-AI")

@app.get("/health")
def health():
    return {"status": "ok"}
