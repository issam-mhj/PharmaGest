import React from "react";

const MedicamentFilters = ({ filters, categories, onChange, onReset }) => {
  return (
    <section className="card filter-grid">
      <div>
        <label>Recherche</label>
        <input
          value={filters.search}
          onChange={(event) => onChange({ search: event.target.value, page: 1 })}
          placeholder="Nom, DCI, forme, dosage"
        />
      </div>

      <div>
        <label>Catégorie</label>
        <select
          value={filters.categorie}
          onChange={(event) => onChange({ categorie: event.target.value, page: 1 })}
        >
          <option value="">Toutes</option>
          {categories.map((category) => (
            <option key={category.id} value={category.id}>
              {category.nom}
            </option>
          ))}
        </select>
      </div>

      <div>
        <label>Ordonnance</label>
        <select
          value={filters.ordonnance_requise}
          onChange={(event) => onChange({ ordonnance_requise: event.target.value, page: 1 })}
        >
          <option value="">Tous</option>
          <option value="true">Oui</option>
          <option value="false">Non</option>
        </select>
      </div>

      <div className="filter-actions">
        <button type="button" className="btn-secondary" onClick={onReset}>
          Réinitialiser
        </button>
      </div>
    </section>
  );
};

export default MedicamentFilters;