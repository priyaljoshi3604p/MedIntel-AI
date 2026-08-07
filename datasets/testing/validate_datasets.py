import json
from pathlib import Path


VITALS_DIR = Path("datasets/sample_vitals")
EXPECTED_DIR = Path("datasets/test_cases")


REQUIRED_INPUT_FIELDS = [
    "case_id",
    "patient",
    "symptoms",
    "vitals",
    "duration",
    "severity"
]


def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file), None

    except json.JSONDecodeError:
        return None, "Invalid JSON format"

    except Exception as e:
        return None, f"Could not read file: {e}"


def validate_input_case(file_path):
    errors = []

    data, error = load_json(file_path)

    if error:
        return [error]

    # Required fields
    for field in REQUIRED_INPUT_FIELDS:
        if field not in data:
            errors.append(f"Missing field: {field}")

    # Patient validation
    patient = data.get("patient")

    if not isinstance(patient, dict):
        errors.append("patient must be an object")

    else:
        if "patient_id" not in patient:
            errors.append("Missing patient.patient_id")

        if "age" not in patient:
            errors.append("Missing patient.age")

        if "sex" not in patient:
            errors.append("Missing patient.sex")

    # Symptoms validation
    if "symptoms" in data:
        if not isinstance(data["symptoms"], list):
            errors.append("symptoms must be a list")

    # Vitals validation
    vitals = data.get("vitals")

    if vitals is not None and not isinstance(vitals, dict):
        errors.append("vitals must be an object or null")

    return errors


def validate_expected_case(file_path, input_case_ids):
    errors = []

    data, error = load_json(file_path)

    if error:
        return [error]

    # case_id
    if "case_id" not in data:
        errors.append("Missing case_id")
    else:
        case_id = data["case_id"]

        if case_id not in input_case_ids:
            errors.append(
                f"No matching input case found for {case_id}"
            )

    # expected object
    if "expected" not in data:
        errors.append("Missing expected object")
        return errors

    expected = data["expected"]

    if not isinstance(expected, dict):
        errors.append("expected must be an object")
        return errors

    # Expected risk level
    if "risk_level" not in expected:
        errors.append("Missing expected.risk_level")

    return errors


def main():

    total_errors = 0

    print("MedIntel-AI Dataset Validator")
    print("=" * 45)

    # --------------------------------
    # Validate input cases
    # --------------------------------

    input_files = sorted(VITALS_DIR.glob("*.json"))

    if not input_files:
        print("❌ No input JSON files found.")
        return

    input_case_ids = set()

    print("\nINPUT CASES")
    print("-" * 45)

    for file_path in input_files:

        data, error = load_json(file_path)

        if data and "case_id" in data:
            input_case_ids.add(data["case_id"])

        errors = validate_input_case(file_path)

        if errors:

            print(f"\n❌ {file_path}")

            for error in errors:
                print(f"   - {error}")

            total_errors += len(errors)

        else:

            print(f"✅ {file_path}")

    # --------------------------------
    # Validate expected outputs
    # --------------------------------

    expected_files = sorted(EXPECTED_DIR.glob("*_expected.json"))

    print("\nEXPECTED OUTPUTS")
    print("-" * 45)

    for file_path in expected_files:

        errors = validate_expected_case(
            file_path,
            input_case_ids
        )

        if errors:

            print(f"\n❌ {file_path}")

            for error in errors:
                print(f"   - {error}")

            total_errors += len(errors)

        else:

            print(f"✅ {file_path}")

    # --------------------------------
    # Check matching expected outputs
    # --------------------------------

    expected_case_ids = set()

    for file_path in expected_files:

        data, error = load_json(file_path)

        if data and "case_id" in data:
            expected_case_ids.add(data["case_id"])

    print("\nCASE MATCHING")
    print("-" * 45)

    missing_expected = input_case_ids - expected_case_ids

    if missing_expected:

        for case_id in sorted(missing_expected):

            print(
                f"❌ Missing expected output for {case_id}"
            )

            total_errors += 1

    else:

        print("✅ Every input case has an expected output.")

    # --------------------------------
    # Final result
    # --------------------------------

    print("\n" + "=" * 45)

    if total_errors == 0:

        print("🎉 All dataset validation checks passed!")

    else:

        print(
            f"❌ Validation completed with "
            f"{total_errors} error(s)."
        )


if __name__ == "__main__":
    main()