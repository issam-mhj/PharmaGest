import React from "react";

const MedicamentList = ({ medicaments, onEdit, onArchive }) => {
  return (
    <section className="card-grid">
      {medicaments.map((item) => (
        <article className="card" key={item.id}>
          <div className="card-title-row">
            <strong>{item.nom}</strong>
            {item.est_en_alerte ? <span className="badge-alert">Stock bas</span> : <span className="badge-ok">OK</span>}
          </div>
          <div>DCI: {item.dci}</div>
          <div>Stock: {item.stock_actuel}</div>
          <div>Seuil: {item.stock_minimum}</div>
          <div>Prix vente: {item.prix_vente}</div>

          <div className="item-actions">
            <button type="button" onClick={() => onEdit(item)}>
              Modifier
            </button>
            <button type="button" className="btn-danger" onClick={() => onArchive(item)}>
              Archiver
            </button>
          </div>
        </article>
      ))}
    </section>
  );
};

export default MedicamentList;