from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import shutil
import os

from agents.report_agent import report_agent

router = APIRouter()

UPLOAD_FOLDER = "uploads/pdfs"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@router.post("/report")

async def analyze_report(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = report_agent.analyze(file_path)

    return result