import React from "react";

function RiskMeter() {
  return (
    <section className="card risk-card">
      <p className="eyebrow">Risk assessment</p>
      <h3>Moderate Risk</h3>
      <p className="risk-score">68%</p>
      <div className="meter">
        <div className="meter-fill" style={{ width: "68%" }}></div>
      </div>
      <p>Priority: Urgent follow-up within 2 hours.</p>
    </section>
  );
}

export default RiskMeter;