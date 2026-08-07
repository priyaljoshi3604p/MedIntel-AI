import os
from dataclasses import dataclass

@dataclass
class Patient:
    id: str = ""
    name: str = ""
    age: int = 0
    sex: str = ""
    history: str = ""
