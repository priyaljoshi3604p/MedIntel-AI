import { useState } from "react";
import { Routes, Route, useLocation, useNavigate } from "react-router-dom";
import Navbar from "./components/Navbar";
import Landing from "./pages/Landing";
import Dashboard from "./pages/Dashboard";
import Intake from "./pages/Intake";
import PatientDetail from "./pages/PatientDetail";
import Analytics from "./pages/Analytics";
import Compliance from "./pages/Compliance";

function App() {
  const [activePage, setActivePage] = useState("landing");
  const location = useLocation();
  const navigate = useNavigate();

  const routeToPage = {
    "/": "landing",
    "/dashboard": "dashboard",
    "/intake": "intake",
    "/analytics": "analytics",
    "/compliance": "compliance",
  };

  const currentPage = routeToPage[location.pathname] || "dashboard";

  const handleNav = (page) => {
    const routeMap = {
      landing: "/",
      dashboard: "/dashboard",
      intake: "/intake",
      analytics: "/analytics",
      compliance: "/compliance",
    };
    setActivePage(page);
    navigate(routeMap[page]);
  };

  return (
    <div className="app-shell no-sidebar">
      <div className="main-panel full-width">
        <Navbar activePage={currentPage} setActivePage={handleNav} />
        <main className="content">
          <Routes>
            <Route path="/" element={<Landing />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/intake" element={<Intake />} />
            <Route path="/patient/:id" element={<PatientDetail />} />
            <Route path="/analytics" element={<Analytics />} />
            <Route path="/compliance" element={<Compliance />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

export default App;