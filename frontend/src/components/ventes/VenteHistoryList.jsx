import React from "react";

const VenteHistoryList = ({ ventes, onViewDetail, onCancel, cancelling }) => {
  return (
    <div className="card-grid">
      {ventes.map((vente) => (
        <article key={vente.id} className="card">
          <strong>{vente.reference}</strong>
          <div>Statut: {vente.statut}</div>
          <div>Date: {new Date(vente.date_vente).toLocaleString()}</div>
          <div>Total TTC: {vente.total_ttc}</div>

          <div className="item-actions">
            <button type="button" onClick={() => onViewDetail(vente.id)}>
              Détails
            </button>
            <button
              type="button"
              className="btn-danger"
              onClick={() => onCancel(vente)}
              disabled={cancelling || vente.statut === "ANNULEE"}
            >
              {vente.statut === "ANNULEE" ? "Déjà annulée" : "Annuler"}
            </button>
          </div>
        </article>
      ))}
    </div>
  );
};

export default VenteHistoryList;