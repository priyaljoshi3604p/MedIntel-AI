import json
from pathlib import Path


DATASET_DIR = Path("datasets/sample_vitals")


def load_case(case_id):
    """
    Load a synthetic patient case by case ID.
    """

    file_path = DATASET_DIR / f"{case_id.lower()}.json"

    if not file_path.exists():
        raise FileNotFoundError(
            f"Case not found: {case_id}"
        )

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_all_cases():
    """
    Load all available synthetic patient cases.
    """

    cases = []

    for file_path in sorted(DATASET_DIR.glob("*.json")):

        with open(file_path, "r", encoding="utf-8") as file:
            cases.append(json.load(file))

    return cases


if __name__ == "__main__":

    cases = load_all_cases()

    print(f"Loaded {len(cases)} cases.")

    for case in cases:
        print(
            f"{case['case_id']} → "
            f"{case['expected_risk']}"
        )