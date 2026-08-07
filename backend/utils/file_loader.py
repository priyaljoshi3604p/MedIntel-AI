from pathlib import Path


PROMPT_DIR = Path(__file__).resolve().parent.parent / "prompts"


def load_prompt(filename):

    with open(PROMPT_DIR / filename, "r", encoding="utf-8") as f:

        return f.read()