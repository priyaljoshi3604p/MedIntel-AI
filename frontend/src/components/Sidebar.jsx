import React from "react";

function Sidebar({ activePage, setActivePage }) {
  const items = [
    { id: "landing", label: "Home" },
    { id: "dashboard", label: "Triage Queue" },
    { id: "intake", label: "Patient Intake" },
    { id: "analytics", label: "Analytics" },
    { id: "compliance", label: "Compliance" },
  ];

  function getIcon(id) {
    switch (id) {
      case "landing":
        return (
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">
            <path d="M3 10.5 12 3l9 7.5v8a2 2 0 0 1-2 2h-4v-6H9v6H5a2 2 0 0 1-2-2v-8Z" stroke="#4a78ff" strokeWidth="1.2" strokeLinejoin="round" />
          </svg>
        );
      case "dashboard":
        return (
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">
            <rect x="3" y="3" width="8" height="8" rx="1" fill="#4a78ff" />
            <rect x="13" y="3" width="8" height="5" rx="1" fill="#2b5eff" />
            <rect x="13" y="10" width="8" height="11" rx="1" fill="#2b5eff" />
            <rect x="3" y="13" width="8" height="8" rx="1" fill="#69a4ff" />
          </svg>
        );
      case "intake":
        return (
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">
            <rect x="4" y="3" width="12" height="18" rx="2" stroke="#4a78ff" strokeWidth="1.2" />
            <path d="M8 7h6M8 11h8" stroke="#4a78ff" strokeWidth="1.2" strokeLinecap="round" />
          </svg>
        );
      case "analytics":
        return (
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">
            <path d="M3 12h6l3 6 6-12" stroke="#4a78ff" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        );
      case "compliance":
        return (
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">
            <path d="M12 15.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z" stroke="#4a78ff" strokeWidth="1.2" />
            <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09a1.65 1.65 0 0 0-1-1.51 1.65 1.65 0 0 0-1.82.33l-.06.06A2 2 0 1 1 2.28 18.9l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09a1.65 1.65 0 0 0 1.51-1 1.65 1.65 0 0 0-.33-1.82L4.41 4.2A2 2 0 1 1 7.24 1.37l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V1a2 2 0 1 1 4 0v.09c.06.6.4 1.1 1 1.51h.09a1.65 1.65 0 0 0 1.82-.33l.06-.06A2 2 0 1 1 21.72 5.1l-.06.06a1.65 1.65 0 0 0-.33 1.82V8a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z" stroke="#4a78ff" strokeWidth="0.9" />
          </svg>
        );
      default:
        return null;
    }
  }

  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <div className="brand-icon large">MI</div>
        <h2>MedIntel</h2>
        <p>Clinical AI Assistant</p>
      </div>
      <ul className="sidebar-list">
        {items.map((item) => (
          <li key={item.id}>
            <button
              className={`sidebar-link ${activePage === item.id ? "active" : ""}`}
              onClick={() => setActivePage(item.id)}
              aria-label={item.label}
            >
              <span className="sidebar-icon">{getIcon(item.id)}</span>
              <span className="sidebar-label">{item.label}</span>
            </button>
          </li>
        ))}
      </ul>
      <div className="sidebar-footer">
        <p>Last sync</p>
        <strong>2 min ago</strong>
      </div>
    </aside>
  );
}

export default Sidebar;