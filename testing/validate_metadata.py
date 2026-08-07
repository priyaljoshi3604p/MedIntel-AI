import csv
from pathlib import Path


METADATA = Path("datasets/brain_mri/metadata.csv")


def main():

    print("MedIntel-AI MRI Metadata Validator")
    print("=" * 40)

    errors = []
    count = 0

    with open(METADATA, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            count += 1

            if not row["image"]:
                errors.append("Missing image name")

            if row["label"] not in [
                "glioma",
                "meningioma",
                "pituitary",
                "notumor"
            ]:
                errors.append(
                    f"Invalid label: {row['label']}"
                )

            if row["split"] not in [
                "training",
                "testing"
            ]:
                errors.append(
                    f"Invalid split: {row['split']}"
                )


    if errors:

        for error in errors:
            print("❌", error)

    else:
        print("✅ Metadata is valid")
        print(f"Total records: {count}")

    print("=" * 40)


if __name__ == "__main__":
    main()