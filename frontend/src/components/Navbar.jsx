import React from "react";

function Navbar({ activePage, setActivePage }) {
  const links = [
    { id: "landing", label: "Home" },
    { id: "dashboard", label: "Triage" },
    { id: "intake", label: "Intake" },
    { id: "analytics", label: "Analytics" },
    { id: "compliance", label: "Compliance" },
  ];

  return (
    <header className="navbar">
      <div className="brand-block">
        <div>
          <div className="brand">MedIntel AI</div>
          <div className="brand-subtitle">Clinical Decision Support</div>
        </div>
      </div>
      <nav className="nav-links">
        {links.map((link) => (
          <button
            key={link.id}
            className={`nav-link ${activePage === link.id ? "active" : ""}`}
            onClick={() => setActivePage(link.id)}
          >
            {link.label}
          </button>
        ))}
      </nav>
    </header>
  );
}

export default Navbar;