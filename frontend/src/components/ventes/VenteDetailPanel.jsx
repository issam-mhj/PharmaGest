import React from "react";

const VenteDetailPanel = ({ vente, loading, error }) => {
  if (!vente && !loading && !error) {
    return <div className="card">Sélectionnez une vente pour afficher ses détails.</div>;
  }

  if (loading) {
    return <div className="card">Chargement du détail de la vente...</div>;
  }

  if (error) {
    return <div className="card">Erreur lors du chargement du détail.</div>;
  }

  return (
    <section className="card">
      <h3>Détail vente {vente.reference}</h3>
      <div>Statut: {vente.statut}</div>
      <div>Total TTC: {vente.total_ttc}</div>
      <div>Notes: {vente.notes || "-"}</div>
      <hr />
      <div className="detail-lines">
        {vente.lignes?.map((ligne) => (
          <div className="detail-line" key={ligne.id}>
            <strong>{ligne.medicament_nom}</strong>
            <span>Qté: {ligne.quantite}</span>
            <span>PU: {ligne.prix_unitaire}</span>
            <span>Sous-total: {ligne.sous_total}</span>
          </div>
        ))}
      </div>
    </section>
  );
};

export default VenteDetailPanel;