import subprocess
import sys


TESTS = [
    "datasets/testing/validate_datasets.py",
    "datasets/testing/validate_edge_cases.py",
    "datasets/testing/validate_brain_mri.py",
    "testing/validate_metadata.py",
    "testing/mri_evaluator.py"
]




def main():
    print("=============================================")
    print("       MedIntel-AI DATASET TEST RUNNER")
    print("=============================================")

    all_passed = True

    for test in TESTS:

        print(f"\n▶ Running: {test}")
        print("-" * 45)

        result = subprocess.run(
            [sys.executable, test]
        )

        if result.returncode != 0:
            all_passed = False

    print("\n=============================================")

    if all_passed:
        print("🎉 ALL DATASET TESTS PASSED!")
        return 0

    print("❌ SOME DATASET TESTS FAILED.")
    return 1


if __name__ == "__main__":
    sys.exit(main())