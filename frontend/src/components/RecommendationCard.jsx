import React from "react";

function RecommendationCard() {
  const recommendations = [
    "Administer oxygen monitoring and recheck vitals every 15 mins",
    "Consult ICU team for escalation review",
    "Prepare medication and imaging summary for the care team",
  ];

  return (
    <section className="card">
      <p className="eyebrow">Recommendations</p>
      <ul className="recommendation-list">
        {recommendations.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </section>
  );
}

export default RecommendationCard;