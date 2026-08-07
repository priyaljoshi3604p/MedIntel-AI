import React from "react";

function Analyze() {
  return (
    <div className="page-card">
      <p className="eyebrow">Analysis workspace</p>
      <h2>Review the latest findings</h2>
      <p>The AI system is combining symptom data, OCR report extractions, and risk scoring to suggest the next best action.</p>
      <div className="detail-box">
        <h3>Detected signals</h3>
        <ul>
          <li>Elevated respiratory concern</li>
          <li>Potential medication interaction</li>
          <li>Recent abnormal imaging upload</li>
        </ul>
      </div>
    </div>
  );
}

export default Analyze;