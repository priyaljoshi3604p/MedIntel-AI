import React, { useState } from "react";

function Compliance() {
  const [role, setRole] = useState("Clinician");

  return (
    <div className="page-grid">
      <section className="hero-card">
        <p className="eyebrow">Privacy and compliance</p>
        <h2>Role-aware access and audit controls</h2>
        <p>Visual-only controls to demonstrate governance, audit, and anonymization behavior.</p>
      </section>

      <section className="card">
        <h3>Current role</h3>
        <select className="select-control" value={role} onChange={(e) => setRole(e.target.value)}>
          <option>Clinician</option>
          <option>Admin</option>
          <option>Paramedic</option>
        </select>
        <div className="pill-row">
          <span className="pill">{role} view</span>
          <span className="pill">Audit enabled</span>
          <span className="pill">Anonymized data</span>
        </div>
      </section>

      <section className="card">
        <h3>Mock audit log</h3>
        <table className="audit-table">
          <thead>
            <tr>
              <th>Time</th>
              <th>Action</th>
              <th>Actor</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>09:12</td><td>Patient view</td><td>Clinician</td></tr>
            <tr><td>09:33</td><td>Risk score reviewed</td><td>Admin</td></tr>
            <tr><td>10:01</td><td>Data sync queued</td><td>Paramedic</td></tr>
          </tbody>
        </table>
      </section>

      <section className="card">
        <h3>Data handling</h3>
        <ul className="detail-list">
          <li>Patient identifiers masked before display</li>
          <li>Retention policy set to 90 days</li>
          <li>Offline queue ready for rural or field deployments</li>
        </ul>
      </section>
    </div>
  );
}

export default Compliance;
