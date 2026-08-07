import React from "react";

function Reports() {
  return (
    <div className="page-card">
      <p className="eyebrow">Reports</p>
      <h2>Generated summaries</h2>
      <div className="report-list">
        <div className="detail-box">
          <h3>Triage summary</h3>
          <p>Prepared for nursing handoff.</p>
        </div>
        <div className="detail-box">
          <h3>Clinical note</h3>
          <p>Patient-safe follow-up plan attached.</p>
        </div>
      </div>
    </div>
  );
}

export default Reports;