from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
import shutil
import os

from agents.vision_agent import vision_agent

router = APIRouter()

UPLOAD_FOLDER = "uploads/images"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/vision")

async def analyze_image(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = vision_agent.analyze(file_path)

    return result
