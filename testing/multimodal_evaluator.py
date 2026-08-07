import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from clinical_loader import find_patient


def evaluate_case(patient_id, mri_prediction):
    patient = find_patient(patient_id)

    if patient is None:
        return {
            "status": "ERROR",
            "message": f"Patient {patient_id} not found"
        }

    clinical_risk = []

    if patient["Tumor_Type"].lower() == "malignant":
        clinical_risk.append("malignant tumor")

    if patient["Stage"] in ["III", "IV"]:
        clinical_risk.append("advanced stage")

    if patient["MRI_Result"].lower() == "positive":
        clinical_risk.append("positive MRI result")

    symptoms = [
        patient["Symptom_1"],
        patient["Symptom_2"],
        patient["Symptom_3"]
    ]

    return {
        "status": "OK",
        "patient_id": patient["Patient_ID"],
        "mri_prediction": mri_prediction,
        "tumor_type": patient["Tumor_Type"],
        "histology": patient["Histology"],
        "stage": patient["Stage"],
        "symptoms": ", ".join(symptoms),
        "clinical_risk_factors": clinical_risk,
        "follow_up_required": patient["Follow_Up_Required"]
    }


def main():

    print("MedIntel-AI Multimodal Evaluator")
    print("=" * 50)

    result = evaluate_case(
        patient_id=1,
        mri_prediction="glioma"
    )

    if result["status"] == "ERROR":
        print("❌", result["message"])
        return

    print(f"Patient ID       : {result['patient_id']}")
    print(f"MRI Prediction   : {result['mri_prediction']}")
    print(f"Tumor Type       : {result['tumor_type']}")
    print(f"Histology        : {result['histology']}")
    print(f"Stage            : {result['stage']}")
    print(f"Symptoms         : {result['symptoms']}")

    print(
        f"Clinical Factors : "
        f"{', '.join(result['clinical_risk_factors'])}"
    )

    print(f"Follow-up        : {result['follow_up_required']}")

    print("=" * 50)
    print("✅ Multimodal evaluation completed")


if __name__ == "__main__":
    main()