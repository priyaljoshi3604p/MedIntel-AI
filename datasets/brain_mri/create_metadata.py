import csv
from pathlib import Path


BASE_DIR = Path("datasets/brain_mri")

OUTPUT_FILE = BASE_DIR / "metadata.csv"


classes = [
    "glioma",
    "meningioma",
    "pituitary",
    "notumor"
]


rows = []


for split in ["training", "testing"]:

    folder = BASE_DIR / split

    for label in classes:

        class_folder = folder / label

        for image in class_folder.iterdir():

            if image.is_file():

                rows.append({
                    "image": image.name,
                    "label": label,
                    "split": split
                })


with open(OUTPUT_FILE, "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["image", "label", "split"]
    )

    writer.writeheader()
    writer.writerows(rows)


print("Metadata created!")
print(f"Total images indexed: {len(rows)}")