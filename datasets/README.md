# MedIntel-AI Datasets

## Overview

This directory contains synthetic datasets, reference-source
metadata, test cases, and validation tools used during development
of the MedIntel-AI clinical decision-support prototype.

The current datasets are intended for software development,
testing, evaluation, and demonstration only.

They are not real patient records and must not be used for
clinical diagnosis or treatment.

---

## Directory Structure

```text
datasets/
│
├── README.md
├── data_dictionary.md
│
├── medical_guidelines/
│   ├── README.md
│   ├── sources.md
│   ├── manifest.json
│   ├── documents/
│   └── processed/
│
├── sample_reports/
│   ├── case_001.txt
│   ├── case_002.txt
│   └── case_003.txt
│
├── sample_images/
│   └── README.md
│
├── sample_audio/
│   └── case_001_transcript.txt
│
├── sample_vitals/
│   ├── case_001.json
│   ├── case_002.json
│   └── case_003.json
│
├── test_cases/
│   ├── README.md
│   ├── case_001_expected.json
│   ├── case_002_expected.json
│   ├── case_003_expected.json
│   │
│   └── edge_cases/
│       ├── missing_vitals.json
│       ├── missing_vitals_expected.json
│       ├── invalid_vitals.json
│       ├── invalid_vitals_expected.json
│       ├── conflicting_information.json
│       ├── conflicting_information_expected.json
│       ├── poor_quality_input.json
│       └── poor_quality_input_expected.json
│
└── testing/
    ├── validate_datasets.py
    ├── validate_edge_cases.py
    ├── run_all_tests.py
    └── TEST_REPORT.md
```

---

## Dataset Categories

### Sample Vitals

Contains synthetic patient cases with symptoms and vital signs.

Current cases:

* CASE_001 — High reference risk
* CASE_002 — Low reference risk
* CASE_003 — Moderate reference risk

---

### Sample Reports

Contains synthetic clinical-style reports corresponding to the
sample patient cases.

The reports allow the system to test document-based input alongside
structured vital-sign data.

---

### Sample Audio

Contains synthetic transcripts representing information that could
be obtained from a patient audio input.

Actual patient audio should not be committed to the repository.

---

### Sample Images

Reserved for appropriately licensed and de-identified medical
images.

Images must not be falsely associated with a synthetic patient
unless the source dataset explicitly establishes that relationship.

---

### Medical Guidelines

Contains metadata and organization for authoritative reference
material intended for the knowledge retrieval/RAG component.

Every reference should be traceable to its original source and
checked for appropriate usage rights.

---

### Test Cases

Contains expected outputs used to evaluate system behavior.

Normal cases test different reference risk levels.

Edge cases test situations such as:

* Missing information
* Invalid values
* Conflicting information
* Poor-quality input

---

## Automated Testing

Run all dataset validation tests with:

```bash
python3 datasets/testing/run_all_tests.py
```

The test runner validates:

* JSON structure
* Required fields
* Patient information
* Symptoms format
* Vital-sign structure
* Expected outputs
* Case matching
* Edge-case structure

---

## Current Test Status

The current synthetic dataset passes all implemented validation
checks.

```text
Normal dataset validation       PASS
Expected-output validation      PASS
Case matching                   PASS
Edge-case validation            PASS
Master test runner              PASS
```

---

## Data Safety

No real patient-identifiable information should be committed to
this repository.

Synthetic data is used during development to reduce privacy and
data-governance risks.

Clinical reference material must be handled according to its
applicable licensing and usage requirements.

---

## Important Limitation

Passing dataset validation only confirms that the test data is
structurally valid and internally consistent.

It does not demonstrate clinical accuracy, diagnostic capability,
or suitability for real-world medical decision-making.
