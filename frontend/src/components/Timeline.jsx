import React from "react";

function Timeline() {
  const events = [
    { time: "09:15", title: "Report uploaded", detail: "Lab results processed" },
    { time: "09:40", title: "Symptoms reviewed", detail: "High severity signs flagged" },
    { time: "10:00", title: "Recommendation drafted", detail: "Escalation suggested" },
  ];

  return (
    <section className="card">
      <p className="eyebrow">Timeline</p>
      <ul className="timeline-list">
        {events.map((event) => (
          <li key={event.time} className="timeline-item">
            <strong>{event.time}</strong>
            <div>
              <p>{event.title}</p>
              <span>{event.detail}</span>
            </div>
          </li>
        ))}
      </ul>
    </section>
  );
}

export default Timeline;