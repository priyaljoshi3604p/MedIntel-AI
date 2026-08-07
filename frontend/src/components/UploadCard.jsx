import React from "react";

function UploadCard() {
  return (
    <section className="card upload-card">
      <div>
        <p className="eyebrow">New intake</p>
        <h3>Upload patient data</h3>
        <p>Drop reports, images, or audio to generate an AI-assisted assessment in seconds.</p>
      </div>
      <button className="action-btn">Upload files</button>
    </section>
  );
}

export default UploadCard;