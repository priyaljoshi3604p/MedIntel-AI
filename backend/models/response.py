from dataclasses import dataclass

@dataclass
class ResponseModel:
    status: str = "ok"
    message: str = ""
    data: dict | None = None
