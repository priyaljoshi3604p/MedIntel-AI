import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from clinical_loader import find_patient


def check_consistency(patient_id):
    patient = find_patient(patient_id)

    if patient is None:
        return {
            "status": "ERROR",
            "message": f"Patient {patient_id} not found"
        }

    warnings = []

    tumor_type = patient["Tumor_Type"].lower()
    histology = patient["Histology"].lower()
    stage = patient["Stage"]

    # Flag potentially conflicting clinical information.
    if tumor_type == "benign" and histology == "glioblastoma":
        warnings.append(
            "Benign tumor type conflicts with glioblastoma histology"
        )

    if stage not in ["I", "II", "III", "IV"]:
        warnings.append(
            f"Unexpected tumor stage: {stage}"
        )

    if patient["MRI_Result"].lower() not in ["positive", "negative"]:
        warnings.append(
            f"Unexpected MRI result: {patient['MRI_Result']}"
        )

    if warnings:
        return {
            "status": "WARNING",
            "patient_id": patient["Patient_ID"],
            "warnings": warnings
        }

    return {
        "status": "OK",
        "patient_id": patient["Patient_ID"],
        "warnings": []
    }


def main():
    print("MedIntel-AI Clinical Consistency Checker")
    print("=" * 50)

    for patient_id in [1, 2, 3]:
        result = check_consistency(patient_id)

        print(f"\nPatient {patient_id}:")

        if result["status"] == "ERROR":
            print("❌", result["message"])

        elif result["status"] == "WARNING":
            print("⚠️ Clinical inconsistency detected")

            for warning in result["warnings"]:
                print("   ⚠️", warning)

        else:
            print("✅ No consistency warnings")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()