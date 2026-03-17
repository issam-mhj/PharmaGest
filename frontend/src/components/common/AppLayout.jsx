import React from "react";
import { NavLink, Outlet } from "react-router-dom";

import GlobalRequestStatus from "./GlobalRequestStatus";

const AppLayout = () => {
  return (
    <div className="app-layout">
      <header className="topbar">
        <strong>PharmaManager</strong>
        <nav className="nav-links">
          <NavLink to="/dashboard" className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}>
            Dashboard
          </NavLink>
          <NavLink to="/medicaments" className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}>
            Médicaments
          </NavLink>
          <NavLink to="/ventes" className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}>
            Ventes
          </NavLink>
        </nav>
      </header>

      <GlobalRequestStatus />

      <main className="page-container">
        <Outlet />
      </main>
    </div>
  );
};

export default AppLayout;