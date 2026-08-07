import json
from pathlib import Path

from prediction_interface import get_prediction


VITALS_DIR = Path("datasets/sample_vitals")
EXPECTED_DIR = Path("datasets/test_cases")


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_expected_case(case_id):
    file_path = EXPECTED_DIR / f"{case_id.lower()}_expected.json"

    if not file_path.exists():
        raise FileNotFoundError(
            f"Expected result not found for {case_id}"
        )

    return load_json(file_path)


def evaluate_risk(predicted_risk, expected_risk):
    predicted = predicted_risk.lower().strip()
    expected = expected_risk.lower().strip()

    return {
        "predicted_risk": predicted,
        "expected_risk": expected,
        "correct": predicted == expected
    }


def print_evaluation(case_id, result):
    print(f"\nCase: {case_id}")
    print("-" * 30)

    print(f"Predicted Risk : {result['predicted_risk']}")
    print(f"Expected Risk  : {result['expected_risk']}")

    if result["correct"]:
        print("Result         : PASS ✅")
    else:
        print("Result         : FAIL ❌")


def main():

    files = sorted(VITALS_DIR.glob("*.json"))

    total = 0
    passed = 0

    print("MedIntel-AI Evaluation Runner")
    print("=" * 40)

    for file_path in files:

        case_data = load_json(file_path)

        case_id = case_data["case_id"]

        expected_data = load_expected_case(case_id)

        expected_risk = expected_data["expected"]["risk_level"]

        # Get prediction through the AI prediction interface
        predicted_risk = get_prediction(case_data)

        result = evaluate_risk(
            predicted_risk,
            expected_risk
        )

        print_evaluation(case_id, result)

        total += 1

        if result["correct"]:
            passed += 1

    print("\n" + "=" * 40)

    print(
        f"Evaluation Summary: {passed}/{total} passed"
    )

    if passed == total:
        print("🎉 ALL EVALUATIONS PASSED!")
    else:
        print("❌ SOME EVALUATIONS FAILED.")


if __name__ == "__main__":
    main()