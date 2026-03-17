import React from "react";
import { Navigate, Route, Routes } from "react-router-dom";

import AppLayout from "./components/common/AppLayout";
import DashboardPage from "./pages/DashboardPage";
import MedicamentsPage from "./pages/MedicamentsPage";
import VentesPage from "./pages/VentesPage";

const App = () => {
  return (
    <Routes>
      <Route element={<AppLayout />}>
        <Route path="/" element={<Navigate to="/dashboard" replace />} />
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/medicaments" element={<MedicamentsPage />} />
        <Route path="/ventes" element={<VentesPage />} />
      </Route>
    </Routes>
  );
};

export default App;
