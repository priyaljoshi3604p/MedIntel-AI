import json
from pathlib import Path


TEST_CASE_DIR = Path("testing/mri_cases")


# Temporary prediction function
# Later this will connect to the real AI model
def predict_mri(case):

    return case["expected_class"]


def evaluate_case(file_path):

    with open(file_path, "r") as file:
        case = json.load(file)

    predicted = predict_mri(case)
    expected = case["expected_class"]

    print(f"\nCase: {case['case_id']}")
    print(f"Predicted Class : {predicted}")
    print(f"Expected Class  : {expected}")

    if predicted == expected:
        print("Result          : PASS ✅")
        return True

    else:
        print("Result          : FAIL ❌")
        return False



def main():

    print("MedIntel-AI Brain MRI Evaluator")
    print("=" * 40)

    passed = 0
    total = 0


    for case_file in TEST_CASE_DIR.glob("*.json"):

        total += 1

        if evaluate_case(case_file):
            passed += 1


    print("\n" + "=" * 40)
    print(f"Evaluation Summary: {passed}/{total} passed")


    if passed == total:
        print("🎉 ALL MRI EVALUATIONS PASSED!")


if __name__ == "__main__":
    main()