import React from "react";

import MedicamentFilters from "../components/medicaments/MedicamentFilters";
import MedicamentForm from "../components/medicaments/MedicamentForm";
import MedicamentList from "../components/medicaments/MedicamentList";
import { useCategories } from "../hooks/useCategories";
import { useMedicamentMutations } from "../hooks/useMedicamentMutations";
import { useMedicaments } from "../hooks/useMedicaments";

const defaultFilters = {
  search: "",
  categorie: "",
  ordonnance_requise: "",
  page: 1,
  page_size: 6,
};

const MedicamentsPage = () => {
  const [filters, setFilters] = React.useState(defaultFilters);
  const [selectedMedicament, setSelectedMedicament] = React.useState(null);
  const [localError, setLocalError] = React.useState(null);

  const { categories } = useCategories();
  const { medicaments, total, hasNextPage, hasPreviousPage, loading, error } = useMedicaments(filters);
  const { createMedicament, updateMedicament, archiveMedicament, creating, updating, archiving } =
    useMedicamentMutations();

  const handleFilterChange = (partial) => {
    setFilters((current) => ({ ...current, ...partial }));
  };

  const handleResetFilters = () => {
    setFilters(defaultFilters);
  };

  const handleSubmit = async (payload) => {
    try {
      setLocalError(null);
      if (selectedMedicament) {
        await updateMedicament({ id: selectedMedicament.id, payload });
      } else {
        await createMedicament(payload);
      }
      setSelectedMedicament(null);
    } catch (requestError) {
      setLocalError(requestError?.response?.data?.detail || "Échec de l’enregistrement du médicament.");
    }
  };

  const handleArchive = async (medicament) => {
    const confirmed = window.confirm(`Archiver le médicament "${medicament.nom}" ?`);
    if (!confirmed) return;

    try {
      setLocalError(null);
      await archiveMedicament(medicament.id);
      if (selectedMedicament?.id === medicament.id) {
        setSelectedMedicament(null);
      }
    } catch (requestError) {
      setLocalError(requestError?.response?.data?.detail || "Échec de l’archivage du médicament.");
    }
  };

  return (
    <section>
      <h1>Médicaments</h1>
      <p>Total: {total}</p>

      <MedicamentFilters
        filters={filters}
        categories={categories}
        onChange={handleFilterChange}
        onReset={handleResetFilters}
      />

      <MedicamentForm
        categories={categories}
        selectedMedicament={selectedMedicament}
        onSubmit={handleSubmit}
        onCancel={() => setSelectedMedicament(null)}
        submitting={creating || updating}
      />

      {localError ? <div className="status-banner status-error">{localError}</div> : null}
      {error ? (
        <div className="status-banner status-error">{error?.response?.data?.detail || "Erreur de chargement"}</div>
      ) : null}
      {loading ? <div className="status-banner status-loading">Chargement des médicaments...</div> : null}

      <div className="pagination-row">
        <button type="button" disabled={!hasPreviousPage} onClick={() => handleFilterChange({ page: filters.page - 1 })}>
          Précédent
        </button>
        <span>Page {filters.page}</span>
        <button type="button" disabled={!hasNextPage} onClick={() => handleFilterChange({ page: filters.page + 1 })}>
          Suivant
        </button>
      </div>

      <div className="status-inline">{archiving ? "Archivage en cours..." : null}</div>

      <div>
        <h3>Liste</h3>
        <MedicamentList medicaments={medicaments} onEdit={setSelectedMedicament} onArchive={handleArchive} />
      </div>
    </section>
  );
};

export default MedicamentsPage;
