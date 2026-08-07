import React from "react";

function PatientCard() {
  return (
    <section className="card patient-card">
      <p className="eyebrow">Patient snapshot</p>
      <h3>Riya Sharma</h3>
      <p>Age 42 • Female • Room 12B</p>
      <div className="patient-stats">
        <div>
          <strong>BP</strong>
          <span>128/84</span>
        </div>
        <div>
          <strong>HR</strong>
          <span>92 bpm</span>
        </div>
        <div>
          <strong>Temp</strong>
          <span>99.4°F</span>
        </div>
      </div>
      <div className="mini-badge">Stable monitoring</div>
    </section>
  );
}

export default PatientCard;