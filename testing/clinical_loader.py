import csv
from pathlib import Path

DATASET = Path("datasets/clinical/brain_tumor_dataset.csv")


def load_clinical_data():
    """Load all clinical records."""
    with open(DATASET, "r", newline="") as file:
        return list(csv.DictReader(file))


def find_patient(patient_id):
    """Find a patient by ID."""
    for record in load_clinical_data():
        if record["Patient_ID"] == str(patient_id):
            return record

    return None


def search_by_symptom(symptom):
    """Find patients with a matching symptom."""
    symptom = symptom.lower()
    matches = []

    for record in load_clinical_data():
        symptoms = [
            record["Symptom_1"],
            record["Symptom_2"],
            record["Symptom_3"]
        ]

        if any(symptom in s.lower() for s in symptoms):
            matches.append(record)

    return matches


def search_by_tumor_type(tumor_type):
    """Find patients by tumor type."""
    tumor_type = tumor_type.lower()

    return [
        record
        for record in load_clinical_data()
        if record["Tumor_Type"].lower() == tumor_type
    ]


def main():
    print("MedIntel-AI Clinical Dataset Search")
    print("=" * 45)

    records = load_clinical_data()
    print(f"Total clinical records: {len(records)}")

    # Test patient lookup
    patient = find_patient(1)

    if patient:
        print("\nPatient 1 found:")
        print(f"Age: {patient['Age']}")
        print(f"Histology: {patient['Histology']}")
        print(f"Stage: {patient['Stage']}")

    # Test symptom search
    matches = search_by_symptom("seizures")
    print(f"\nPatients with seizures: {len(matches)}")

    # Test tumor-type search
    malignant = search_by_tumor_type("Malignant")
    print(f"Malignant tumor records: {len(malignant)}")

    print("=" * 45)


if __name__ == "__main__":
    main()