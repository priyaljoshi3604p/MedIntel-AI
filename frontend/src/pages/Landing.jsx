import React from "react";
import { Link } from "react-router-dom";

function Landing() {
  return (
    <div className="landing-page">
      <section className="hero-card large">
        <p className="eyebrow">Multimodal clinical intelligence</p>
        <h1>Real-time triage support for critical care pathways.</h1>
        <p>
          MedIntel-AI helps clinicians capture a single structured clinical note and review evidence-based triage insights with no extra vitals or EHR forms.
        </p>
        <div className="hero-actions">
          <Link to="/dashboard" className="action-btn">Enter triage workspace</Link>
          <Link to="/intake" className="action-btn secondary">Open clinical note</Link>
        </div>
        <div className="disclaimer">Decision support only — not a diagnosis. Does not replace licensed clinical judgment.</div>
      </section>

      <section className="feature-section">
        <div className="feature-intro">
          <p className="eyebrow">How it works</p>
          <h2>MedIntel AI works in four simple steps.</h2>
          <p>Enter one structured clinical note, then review AI-assisted guidance for prioritization, escalation, and handoff.</p>
        </div>

        <div className="feature-grid">
          <div className="feature-card">
            <div className="feature-card-number">1</div>
            <h3>Describe the patient</h3>
            <p>Enter symptoms, duration, exam findings, and relevant history in one clean clinical note.</p>
          </div>
          <div className="feature-card">
            <div className="feature-card-number">2</div>
            <h3>Analyze the note</h3>
            <p>AI processing extracts risk signals, acuity drivers, and diagnostic patterns from the note.</p>
          </div>
          <div className="feature-card">
            <div className="feature-card-number">3</div>
            <h3>Review recommendations</h3>
            <p>See prioritized next steps, evidence citations, and suggested care pathways at a glance.</p>
          </div>
          <div className="feature-card">
            <div className="feature-card-number">4</div>
            <h3>Refine as needed</h3>
            <p>Update the clinical summary and let the system refresh insights for the current scenario.</p>
          </div>
        </div>
      </section>

      <section className="promo-card">
        <div>
          <p className="eyebrow">Trusted by care teams</p>
          <h3>Accelerate the shift from intake to informed triage.</h3>
          <p>MedIntel AI makes it easier to capture clinical context in one place and turn it into actionable guidance.</p>
        </div>
        <Link to="/intake" className="action-btn">Start the note</Link>
      </section>
    </div>
  );
}

export default Landing;
