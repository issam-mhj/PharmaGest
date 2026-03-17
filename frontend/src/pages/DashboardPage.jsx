import React from "react";

import { useDashboardStats } from "../hooks/useDashboardStats";

const DashboardPage = () => {
  const { medicamentsCount, alertsCount, ventesTodayCount, alerts, recentSales, loading } = useDashboardStats();

  return (
    <section>
      <h1>Dashboard</h1>

      {loading ? <div className="status-banner status-loading">Chargement des indicateurs dashboard...</div> : null}

      <div className="card-grid">
        <article className="card kpi-card">
          <h3>Médicaments actifs</h3>
          <p className="kpi-value">{medicamentsCount}</p>
        </article>
        <article className="card kpi-card">
          <h3>Alertes stock bas</h3>
          <p className="kpi-value">{alertsCount}</p>
        </article>
        <article className="card kpi-card">
          <h3>Ventes du jour</h3>
          <p className="kpi-value">{ventesTodayCount}</p>
        </article>
      </div>

      <div className="card-grid dashboard-widgets">
        <article className="card">
          <h3>Alertes de stock (top)</h3>
          {alerts.length ? (
            <ul className="widget-list">
              {alerts.slice(0, 5).map((item) => (
                <li key={item.id}>
                  <strong>{item.nom}</strong> — stock {item.stock_actuel} / min {item.stock_minimum}
                </li>
              ))}
            </ul>
          ) : (
            <p>Aucune alerte en cours.</p>
          )}
        </article>

        <article className="card">
          <h3>Dernières ventes</h3>
          {recentSales.length ? (
            <ul className="widget-list">
              {recentSales.map((sale) => (
                <li key={sale.id}>
                  <strong>{sale.reference}</strong> — {sale.statut} — {sale.total_ttc}
                </li>
              ))}
            </ul>
          ) : (
            <p>Aucune vente disponible.</p>
          )}
        </article>
      </div>
    </section>
  );
};

export default DashboardPage;
