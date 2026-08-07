import csv
from pathlib import Path

DATASET = Path("datasets/clinical/brain_tumor_dataset.csv")

REQUIRED_COLUMNS = [
    "Patient_ID",
    "Age",
    "Gender",
    "Tumor_Type",
    "Tumor_Size",
    "Location",
    "Histology",
    "Stage",
    "Symptom_1",
    "Symptom_2",
    "Symptom_3",
    "Radiation_Treatment",
    "Surgery_Performed",
    "Chemotherapy",
    "Survival_Rate",
    "Tumor_Growth_Rate",
    "Family_History",
    "MRI_Result",
    "Follow_Up_Required",
]


def main():
    print("MedIntel-AI Clinical Dataset Validator")
    print("=" * 45)

    if not DATASET.exists():
        print("❌ Clinical dataset not found")
        return 1

    with open(DATASET, "r", newline="") as file:
        reader = csv.DictReader(file)

        missing = [
            column
            for column in REQUIRED_COLUMNS
            if column not in reader.fieldnames
        ]

        if missing:
            print("❌ Missing columns:", missing)
            return 1

        records = list(reader)

    if len(records) != 20000:
        print(f"❌ Expected 20000 records, found {len(records)}")
        return 1

    print("✅ Dataset file exists")
    print("✅ All required columns present")
    print("✅ Exactly 20,000 clinical records found")
    print("=" * 45)
    print("🎉 Clinical dataset validation passed!")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())