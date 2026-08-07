from pathlib import Path

MRI_DIR = Path("datasets/brain_mri")

CLASSES = [
    "glioma",
    "meningioma",
    "pituitary",
    "notumor"
]


def validate_split(split):

    errors = []

    folder = MRI_DIR / split

    if not folder.exists():
        errors.append(f"Missing folder: {folder}")
        return errors

    for cls in CLASSES:

        class_folder = folder / cls

        if not class_folder.exists():
            errors.append(f"Missing class folder: {class_folder}")
            continue

        images = list(class_folder.glob("*"))

        if len(images) == 0:
            errors.append(f"No images found in {class_folder}")

    return errors



def main():

    print("MedIntel-AI Brain MRI Validator")
    print("=" * 40)

    errors = []

    errors += validate_split("training")
    errors += validate_split("testing")


    if errors:

        for error in errors:
            print("❌", error)

    else:

        print("✅ Brain MRI dataset structure valid")


    print("=" * 40)



if __name__ == "__main__":
    main()