import React, { useState } from "react";

function Intake() {
  const [noteText, setNoteText] = useState(
    "Female, 42, severe headaches for 3 months with dizziness and family history of migraines. Reports nausea, photophobia, and intermittent visual aura."
  );
  const [analysis, setAnalysis] = useState(null);

  const generateAnalysis = (text) => {
    const note = text.trim().toLowerCase();
    if (!note) {
      return {
        insight: "Enter a clinical summary before analysis.",
        recommendation: "Provide symptoms, duration, and relevant exam or history findings."
      };
    }

    const has = (pattern) => pattern.test(note);
    let insight = "The note suggests a moderate-acuity presentation that requires further clinical evaluation.";
    let recommendation = "Review the patient history and refine the summary with additional exam findings.";

    if (has(/headache|migraine|photophobia|aura|dizziness/)) {
      insight = "High likelihood of migraine-related headache with neurovascular features.";
      recommendation = "Consider neurologic evaluation and symptom-directed management."
    }

    if (has(/chest pain|shortness of breath|sob|palpitation|pressure/)) {
      insight = "Possible cardiopulmonary etiology with urgency for acute evaluation.";
      recommendation = "Prioritize cardiovascular and respiratory assessment and escalate if unstable."
    }

    if (has(/fever|infection|chills|rigor|sepsis|cough/)) {
      insight = "Clinical features raise concern for an infectious or inflammatory syndrome.";
      recommendation = "Evaluate for infection and consider early supportive care while confirming diagnosis."
    }

    if (has(/abdominal pain|nausea|vomiting|diarrhea|pain in the abdomen/)) {
      insight = "Findings are consistent with an abdominal process requiring focused GI assessment.";
      recommendation = "Review abdominal exam findings and consider imaging or specialist review."
    }

    if (has(/weakness|numbness|speech|slurred|vision loss|confusion/)) {
      insight = "There is concern for a neurologic emergency that needs rapid assessment.";
      recommendation = "Escalate to urgent neurologic evaluation and consider stroke protocols."
    }

    if (has(/severe|acute|worsening|sudden|critical|emergency/)) {
      recommendation = `${recommendation} Act promptly due to high-acuity features.`;
    }

    return { insight, recommendation };
  };

  const handleAnalyze = () => {
    setAnalysis(generateAnalysis(noteText));
  };

  return (
    <div className="note-entry-page">
      <section className="note-hero-card">
        <p className="eyebrow">Clinical note entry</p>
        <h2>Enter a concise patient summary for analysis.</h2>
        <p>Capture age, symptoms, onset, exam findings, and clinical context in one structured note.</p>
      </section>

      <section className="note-card">
        <textarea
          className="note-textarea"
          value={noteText}
          onChange={(e) => setNoteText(e.target.value)}
          placeholder="Type patient details here: age, gender, symptoms, duration, exam findings, relevant history..."
        />
        <button className="action-btn" onClick={handleAnalyze}>Analyze note</button>
        <p className="small-copy">This workflow uses a single clinical note input instead of separate vitals or EHR fields.</p>
      </section>

      {analysis && (
        <section className="card result-card">
          <h3>Analysis result</h3>
          <p><strong>Primary insight:</strong> {analysis.insight}</p>
          <p><strong>Recommended next step:</strong> {analysis.recommendation}</p>
        </section>
      )}
    </div>
  );
}

export default Intake;
