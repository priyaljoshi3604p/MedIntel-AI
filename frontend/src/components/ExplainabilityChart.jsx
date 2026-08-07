import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from "recharts";

function ExplainabilityChart({ breakdown }) {
  return (
    <div className="chart-card">
      <h4>Contribution breakdown</h4>
      <ResponsiveContainer width="100%" height={220}>
        <BarChart data={breakdown}>
          <CartesianGrid strokeDasharray="3 3" stroke="#203754" />
          <XAxis dataKey="name" stroke="#8fb3ff" />
          <YAxis stroke="#8fb3ff" />
          <Tooltip />
          <Bar dataKey="value" fill="#4a78ff" radius={[6, 6, 0, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default ExplainabilityChart;
