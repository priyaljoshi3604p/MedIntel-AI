import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid, PieChart, Pie, Cell } from "recharts";
import mockPatients from "../data/mockPatients";

const riskData = [
  { name: "Immediate", value: 2 },
  { name: "High", value: 2 },
  { name: "Moderate", value: 2 },
];

const COLORS = ["#ff5b5b", "#ffb347", "#4a78ff"];

function Analytics() {
  const total = mockPatients.length;
  const averageDecision = "1.4s";

  return (
    <div className="page-grid">
      <section className="hero-card">
        <p className="eyebrow">Analytics</p>
        <h2>Operational overview</h2>
        <p>Mock performance statistics for the triage workflow and patient mix.</p>
      </section>

      <section className="card">
        <h3>Key metrics</h3>
        <div className="stat-grid">
          <div className="stat-card"><strong>{total}</strong><span>Patients triaged</span></div>
          <div className="stat-card"><strong>{averageDecision}</strong><span>Avg. decision time</span></div>
          <div className="stat-card"><strong>92%</strong><span>Recommendation confidence</span></div>
        </div>
      </section>

      <section className="card chart-card">
        <h3>Severity distribution</h3>
        <ResponsiveContainer width="100%" height={220}>
          <BarChart data={riskData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#203754" />
            <XAxis dataKey="name" stroke="#8fb3ff" />
            <YAxis stroke="#8fb3ff" />
            <Tooltip />
            <Bar dataKey="value" fill="#4a78ff" radius={[6, 6, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </section>

      <section className="card chart-card">
        <h3>Risk mix</h3>
        <ResponsiveContainer width="100%" height={220}>
          <PieChart>
            <Pie data={riskData} dataKey="value" nameKey="name" outerRadius={80}>
              {riskData.map((entry, index) => (
                <Cell key={entry.name} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </section>
    </div>
  );
}

export default Analytics;
