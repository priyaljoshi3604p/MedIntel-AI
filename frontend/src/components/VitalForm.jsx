import React from "react";

function VitalForm() {
  return (
    <section className="card">
      <p className="eyebrow">Vital entry</p>
      <form className="vital-form">
        <input placeholder="Oxygen saturation" />
        <input placeholder="Respiratory rate" />
        <button type="button" className="action-btn">Save</button>
      </form>
    </section>
  );
}

export default VitalForm;