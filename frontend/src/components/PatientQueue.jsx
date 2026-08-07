import React from "react";
import mockPatients from "../data/mockPatients";

function PatientQueue({ selectedPatient, onSelect }) {
  const sortedPatients = [...mockPatients].sort((a, b) => b.severity - a.severity);

  return (
    <section className="card">
      <div className="section-header">
        <div>
          <p className="eyebrow">Live queue</p>
          <h3>Patient triage queue</h3>
        </div>
        <span className="pill">Simulated refresh</span>
      </div>
      <div className="queue-list">
        {sortedPatients.map((patient) => (
          <button
            key={patient.id}
            className={`queue-item ${selectedPatient?.id === patient.id ? "selected" : ""}`}
            onClick={() => onSelect(patient)}
          >
            <div className="queue-main">
              <strong>{patient.name}</strong>
              <span>{patient.location}</span>
            </div>
            <div className="queue-meta">
              <span className={`severity-badge severity-${patient.severity}`}>{patient.acuity}</span>
              <span>{patient.triageStatus}</span>
            </div>
          </button>
        ))}
      </div>
    </section>
  );
}

export default PatientQueue;
