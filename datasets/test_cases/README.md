# MedIntel-AI Test Cases

This directory contains synthetic test cases used to evaluate the
MedIntel-AI system.

## Test Categories

### 1. High-Risk Cases

Cases where the system should identify a potentially urgent
presentation and recommend appropriate clinical escalation.

### 2. Moderate-Risk Cases

Cases requiring clinical attention but with less immediate concern.

### 3. Low-Risk Cases

Cases where no immediate emergency features are present.

### 4. Edge Cases

Cases designed to test system robustness, including:

* Missing vital signs
* Incomplete symptoms
* Invalid values
* Conflicting information
* Unclear input
* Unsupported files
* Poor-quality images

## Evaluation Principle

Each test case contains reference expectations used to evaluate
the AI system's output.

The reference expectations are not medical diagnoses and should
not be used as treatment instructions.

## Data Safety

All test cases are synthetic and created for software development,
testing, and demonstration only.
