import React from "react";

import VenteDetailPanel from "../components/ventes/VenteDetailPanel";
import VenteForm from "../components/ventes/VenteForm";
import VenteHistoryList from "../components/ventes/VenteHistoryList";
import { useMedicaments } from "../hooks/useMedicaments";
import { useVenteDetail } from "../hooks/useVenteDetail";
import { useVenteMutations } from "../hooks/useVenteMutations";
import { useVentes } from "../hooks/useVentes";

const defaultFilters = {
  statut: "",
  page: 1,
  page_size: 6,
};

const VentesPage = () => {
  const [filters, setFilters] = React.useState(defaultFilters);
  const [selectedVenteId, setSelectedVenteId] = React.useState(null);
  const [localError, setLocalError] = React.useState(null);

  const { medicaments } = useMedicaments({ page_size: 100 });
  const { ventes, total, hasNextPage, hasPreviousPage, loading, error } = useVentes(filters);
  const { createVente, cancelVente, creating, cancelling } = useVenteMutations();
  const { vente: selectedVente, loading: detailLoading, error: detailError } = useVenteDetail(selectedVenteId);

  const handleCreateSale = async (payload) => {
    try {
      setLocalError(null);
      const created = await createVente(payload);
      setSelectedVenteId(created.id);
    } catch (requestError) {
      setLocalError(requestError?.response?.data?.detail || "Échec de création de la vente.");
    }
  };

  const handleCancelSale = async (vente) => {
    const confirmed = window.confirm(`Annuler la vente ${vente.reference} ?`);
    if (!confirmed) return;

    try {
      setLocalError(null);
      await cancelVente(vente.id);
      setSelectedVenteId(vente.id);
    } catch (requestError) {
      setLocalError(requestError?.response?.data?.detail || "Échec de l’annulation de la vente.");
    }
  };

  return (
    <section>
      <h1>Ventes</h1>
      <p>Total: {total}</p>

      <section className="card filter-grid">
        <div>
          <label>Statut</label>
          <select
            value={filters.statut}
            onChange={(event) => setFilters((current) => ({ ...current, statut: event.target.value, page: 1 }))}
          >
            <option value="">Tous</option>
            <option value="COMPLETEE">Complétée</option>
            <option value="ANNULEE">Annulée</option>
          </select>
        </div>
      </section>

      <VenteForm medicaments={medicaments} onSubmit={handleCreateSale} submitting={creating} />

      {localError ? <div className="status-banner status-error">{localError}</div> : null}
      {error ? (
        <div className="status-banner status-error">{error?.response?.data?.detail || "Erreur de chargement"}</div>
      ) : null}
      {loading ? <div className="status-banner status-loading">Chargement des ventes...</div> : null}

      <div className="pagination-row">
        <button type="button" disabled={!hasPreviousPage} onClick={() => setFilters((c) => ({ ...c, page: c.page - 1 }))}>
          Précédent
        </button>
        <span>Page {filters.page}</span>
        <button type="button" disabled={!hasNextPage} onClick={() => setFilters((c) => ({ ...c, page: c.page + 1 }))}>
          Suivant
        </button>
      </div>

      <h3>Historique des ventes</h3>
      <VenteHistoryList
        ventes={ventes}
        onViewDetail={setSelectedVenteId}
        onCancel={handleCancelSale}
        cancelling={cancelling}
      />

      <h3>Détail</h3>
      <VenteDetailPanel vente={selectedVente} loading={detailLoading} error={detailError} />

      <div className="status-inline">{cancelling ? "Annulation en cours..." : null}</div>

      <div className="status-inline">{creating ? "Création de la vente en cours..." : null}</div>

      <div style={{ height: 8 }} />

      <div>
        <small>Astuce: sélectionnez une vente dans l’historique pour voir toutes ses lignes.</small>
      </div>
    </section>
  );
};

export default VentesPage;
