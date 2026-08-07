import React from "react";
import { useParams } from "react-router-dom";
import mockPatients from "../data/mockPatients";
import ExplainabilityChart from "../components/ExplainabilityChart";

function PatientDetail() {
  const { id } = useParams();
  const patient = mockPatients.find((item) => item.id === id) || mockPatients[0];

  return (
    <div className="page-grid detail-view">
      <section className="hero-card">
        <p className="eyebrow">AI analysis</p>
        <h2>{patient.name}</h2>
        <p>{patient.summary}</p>
        <div className="pill-row">
          <span className="pill">{patient.location}</span>
          <span className="pill">{patient.triageStatus}</span>
          <span className="pill">{patient.deployment}</span>
        </div>
      </section>

      <section className="card">
        <h3>Risk indicators</h3>
        <ul className="detail-list">
          <li>Sepsis risk: {(patient.riskScores.sepsis * 100).toFixed(0)}%</li>
          <li>Cardiac event risk: {(patient.riskScores.cardiac * 100).toFixed(0)}%</li>
          <li>Deterioration risk: {(patient.riskScores.deterioration * 100).toFixed(0)}%</li>
          <li>Confidence: {(patient.riskScores.confidence * 100).toFixed(0)}%</li>
        </ul>
      </section>

      <section className="card">
        <h3>Recommendation</h3>
        <p>{patient.recommendation}</p>
        <p className="small-copy">{patient.explanation}</p>
      </section>

      <ExplainabilityChart breakdown={patient.explanationBreakdown} />

      <section className="card">
        <h3>Evidence citations</h3>
        <ul className="detail-list">
          {patient.citations.map((citation) => (
            <li key={citation}>{citation}</li>
          ))}
        </ul>
      </section>

      <section className="card">
        <h3>Clinical note summary</h3>
        <p>Modalities: {patient.modalities.join(" • ")}</p>
        <p>{patient.summary}</p>
      </section>
    </div>
  );
}

export default PatientDetail;
