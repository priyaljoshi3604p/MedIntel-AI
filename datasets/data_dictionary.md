# MedIntel-AI Data Dictionary

## Purpose

Defines the structure and meaning of fields used in the synthetic
clinical test datasets.

---

## Patient Information

| Field                | Type    | Description                           |
| -------------------- | ------- | ------------------------------------- |
| `case_id`            | String  | Unique identifier for a test case     |
| `patient.patient_id` | String  | Synthetic patient identifier          |
| `patient.age`        | Integer | Patient age in years                  |
| `patient.sex`        | String  | Recorded sex of the synthetic patient |

---

## Symptoms

| Field      | Type   | Description                                   |
| ---------- | ------ | --------------------------------------------- |
| `symptoms` | Array  | List of symptoms reported for the case        |
| `duration` | String | Approximate duration of the reported symptoms |
| `severity` | String | Reported severity of symptoms                 |

---

## Vital Signs

| Field                     | Type   | Description                             |
| ------------------------- | ------ | --------------------------------------- |
| `vitals.blood_pressure`   | String | Systolic/diastolic blood pressure       |
| `vitals.heart_rate`       | Number | Heart rate in beats per minute          |
| `vitals.spo2`             | Number | Peripheral oxygen saturation percentage |
| `vitals.temperature_c`    | Number | Body temperature in Celsius             |
| `vitals.respiratory_rate` | Number | Respiratory rate in breaths per minute  |

---

## Evaluation Labels

| Field             | Type   | Description                                          |
| ----------------- | ------ | ---------------------------------------------------- |
| `expected_risk`   | String | Reference risk category used for software evaluation |
| `expected_action` | String | Reference action used to evaluate system behavior    |

These labels are evaluation references for synthetic test cases.
They are not medical diagnoses or treatment instructions.

---

## Example

```json
{
  "case_id": "CASE_001",
  "patient": {
    "patient_id": "DEMO_001",
    "age": 54,
    "sex": "Female"
  },
  "symptoms": [
    "chest discomfort",
    "shortness of breath",
    "dizziness"
  ],
  "vitals": {
    "blood_pressure": "158/96 mmHg",
    "heart_rate": 108,
    "spo2": 93,
    "temperature_c": 37.2,
    "respiratory_rate": 22
  },
  "duration": "45 minutes",
  "severity": "moderate_to_severe",
  "expected_risk": "high",
  "expected_action": "urgent clinical evaluation"
}
```

## Data Safety

All current patient records are synthetic and intended only for
software development, testing, and demonstration.

No real patient-identifiable information should be committed to
the repository.
