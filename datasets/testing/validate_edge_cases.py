import json
from pathlib import Path


EDGE_CASE_DIR = Path("datasets/test_cases/edge_cases")


def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file), None

    except json.JSONDecodeError:
        return None, "Invalid JSON format"

    except Exception as e:
        return None, f"Could not read file: {e}"


def validate_edge_case(file_path):
    errors = []

    data, error = load_json(file_path)

    if error:
        return [error]

    if "case_id" not in data:
        errors.append("Missing case_id")

    return errors


def validate_expected(file_path):
    errors = []

    data, error = load_json(file_path)

    if error:
        return [error]

    if "case_id" not in data:
        errors.append("Missing case_id")

    if "expected" not in data:
        errors.append("Missing expected object")

    return errors


def main():

    total_errors = 0

    print("MedIntel-AI Edge Case Validator")
    print("=" * 45)

    input_files = sorted(
        EDGE_CASE_DIR.glob("*.json")
    )

    # Ignore expected files when finding input cases
    input_files = [
        file for file in input_files
        if not file.name.endswith("_expected.json")
    ]

    expected_files = sorted(
        EDGE_CASE_DIR.glob("*_expected.json")
    )

    print("\nEDGE CASE INPUTS")
    print("-" * 45)

    input_case_ids = set()

    for file_path in input_files:

        data, error = load_json(file_path)

        if data and "case_id" in data:
            input_case_ids.add(data["case_id"])

        errors = validate_edge_case(file_path)

        if errors:

            print(f"❌ {file_path}")

            for error in errors:
                print(f"   - {error}")

            total_errors += len(errors)

        else:

            print(f"✅ {file_path}")

    print("\nEDGE CASE EXPECTED OUTPUTS")
    print("-" * 45)

    expected_case_ids = set()

    for file_path in expected_files:

        data, error = load_json(file_path)

        if data and "case_id" in data:
            expected_case_ids.add(data["case_id"])

        errors = validate_expected(file_path)

        if errors:

            print(f"❌ {file_path}")

            for error in errors:
                print(f"   - {error}")

            total_errors += len(errors)

        else:

            print(f"✅ {file_path}")

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

        print("✅ Every edge case has an expected output.")

    print("\n" + "=" * 45)

    if total_errors == 0:

        print("🎉 All edge-case validation checks passed!")

    else:

        print(
            f"❌ Validation completed with "
            f"{total_errors} error(s)."
        )


if __name__ == "__main__":
    main()