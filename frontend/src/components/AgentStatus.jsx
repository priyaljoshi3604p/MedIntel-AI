import React from "react";

function AgentStatus() {
  const agents = [
    { name: "Intake Agent", status: "Ready" },
    { name: "Symptom Agent", status: "Reviewing" },
    { name: "Decision Agent", status: "Stable" },
  ];

  return (
    <section className="card">
      <p className="eyebrow">Agent pipeline</p>
      <div className="agent-list">
        {agents.map((agent) => (
          <div key={agent.name} className="agent-item">
            <span>{agent.name}</span>
            <span className="pill">{agent.status}</span>
          </div>
        ))}
      </div>
    </section>
  );
}

export default AgentStatus;