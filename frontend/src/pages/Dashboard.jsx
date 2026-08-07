import React, { useState } from "react";
import { Link } from "react-router-dom";
import mockPatients from "../data/mockPatients";
import PatientQueue from "../components/PatientQueue";

function Dashboard() {
  const [selectedPatient, setSelectedPatient] = useState(mockPatients[0]);

  return (
    <div className="page-grid">
      <section className="hero-card">
        <p className="eyebrow">Live triage workspace</p>
        <h2>Multimodal patient queue ranked by urgency.</h2>
        <p>Review high-severity cases, open a patient analysis view, and route recommendations to the care team.</p>
        <div className="pill-row">
          <span className="pill">Decision support only</span>
          <span className="pill">Offline-ready mode</span>
        </div>
      </section>

      <PatientQueue selectedPatient={selectedPatient} onSelect={setSelectedPatient} />

      <section className="card">
        <div className="section-header">
          <div>
            <p className="eyebrow">Selected patient</p>
            <h3>{selectedPatient.name}</h3>
          </div>
          <Link to={`/patient/${selectedPatient.id}`} className="action-btn">Open analysis</Link>
        </div>
        <p>{selectedPatient.summary}</p>
        <p className="small-copy">Acuity: {selectedPatient.acuity} • Deployment: {selectedPatient.deployment}</p>
        <div className="pill-row">
          <span className="pill">Sepsis {Math.round(selectedPatient.riskScores.sepsis * 100)}%</span>
          <span className="pill">Cardiac {Math.round(selectedPatient.riskScores.cardiac * 100)}%</span>
          <span className="pill">Deterioration {Math.round(selectedPatient.riskScores.deterioration * 100)}%</span>
        </div>
      </section>
    </div>
  );
}

export default Dashboard;