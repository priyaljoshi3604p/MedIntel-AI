# MedIntel-AI

MedIntel-AI is an AI-assisted medical intake and analysis platform designed to help clinicians and healthcare workflows process patient data from images, PDFs, audio, vitals, and structured symptoms. The system combines multiple backend agents, retrieval-augmented generation (RAG), OCR, and a modern frontend experience to produce summaries, risk signals, and explainable recommendations.

## Overview

This repository contains:
- A Python-based backend for document ingestion, medical analysis, retrieval, and report generation.
- A React + Vite frontend for uploading data, viewing analyses, and reviewing reports.
- Supporting datasets, prompts, database storage, and documentation.

## Key Features

- Multi-agent medical analysis workflow
- Image, PDF, and audio upload support
- OCR and vision-based parsing for medical documents
- Symptom and vitals-driven triage logic
- RAG-powered knowledge grounding using medical guidelines
- Structured report generation and explanation support
- Dashboard-style frontend experience for patient insights

## Project Structure

`	ext
MedIntel-AI/
+-- backend/
¦   +-- agents/
¦   +-- api/
¦   +-- services/
¦   +-- models/
¦   +-- rag/
¦   +-- uploads/
¦   +-- database/
¦   +-- prompts/
¦   +-- utils/
¦   +-- main.py
¦   +-- requirements.txt
¦   +-- .env
+-- frontend/
¦   +-- src/
¦   +-- public/
¦   +-- package.json
¦   +-- vite.config.js
+-- datasets/
+-- docs/
+-- README.md
`

## Tech Stack

### Backend
- Python
- OCR and vision processing services
- RAG and embedding-based retrieval
- SQLite for local persistence
- Prompt-based agent orchestration

### Frontend
- React
- Vite
- Modern component-based UI structure

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- npm or yarn
- Access to required AI services such as Gemini or related providers (depending on your backend configuration)

### Backend Setup

1. Navigate to the backend folder:
   `ash
   cd backend
   `
2. Create and activate a virtual environment:
   `ash
   python -m venv .venv
   source .venv/bin/activate
   `
   On Windows PowerShell:
   `powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   `
3. Install dependencies:
   `ash
   pip install -r requirements.txt
   `
4. Configure environment variables in .env with the required service credentials.
5. Run the backend application:
   `ash
   python main.py
   `

### Frontend Setup

1. Navigate to the frontend folder:
   `ash
   cd frontend
   `
2. Install dependencies:
   `ash
   npm install
   `
3. Start the development server:
   `ash
   npm run dev
   `

## Environment Variables

Create a backend .env file with variables such as:

`env
GEMINI_API_KEY=your_api_key_here
DATABASE_PATH=database/medintel.db
UPLOAD_DIR=uploads
`

Adjust these values based on your runtime environment and external service configuration.

## Usage Flow

1. Upload a medical image, PDF, or audio file.
2. Enter or review vitals and symptom information.
3. Let the backend agents analyze the input.
4. Review generated reports, decision rationale, and recommendations.

## Documentation

Additional project documentation can be found in the docs/ folder:
- architecture.md
- project_plan.md
- api_documentation.md
- presentation_notes.md

## Notes

This project is structured as a modular AI application and is intended for experimentation, prototyping, and extension. Depending on your deployment and model provider setup, you may need to adjust prompts, services, and environment variables to match your environment.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
