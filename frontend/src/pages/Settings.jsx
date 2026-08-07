import React from "react";

function Settings() {
  return (
    <div className="page-card">
      <p className="eyebrow">Preferences</p>
      <h2>Configure your workflow</h2>
      <div className="detail-box">
        <h3>Automation</h3>
        <p>Auto-generate summaries after uploads</p>
      </div>
      <div className="detail-box">
        <h3>Alerts</h3>
        <p>Notify the care team on moderate and high-risk cases</p>
      </div>
    </div>
  );
}

export default Settings;