import React from "react";

const getMedicamentById = (medicaments, id) =>
  medicaments.find((item) => String(item.id) === String(id));

const VenteForm = ({ medicaments, onSubmit, submitting }) => {
  const [notes, setNotes] = React.useState("");
  const [lignes, setLignes] = React.useState([{ medicamentId: "", quantite: 1 }]);
  const [error, setError] = React.useState(null);

  const addLine = () => setLignes((current) => [...current, { medicamentId: "", quantite: 1 }]);

  const removeLine = (index) => {
    setLignes((current) => current.filter((_, currentIndex) => currentIndex !== index));
  };

  const updateLine = (index, key, value) => {
    setLignes((current) =>
      current.map((line, currentIndex) => (currentIndex === index ? { ...line, [key]: value } : line))
    );
  };

  const computeLineTotal = (line) => {
    const medicament = getMedicamentById(medicaments, line.medicamentId);
    const unitPrice = Number(medicament?.prix_vente || 0);
    return unitPrice * Number(line.quantite || 0);
  };

  const total = lignes.reduce((sum, line) => sum + computeLineTotal(line), 0);

  const validate = () => {
    if (!lignes.length) return "Ajoutez au moins une ligne de vente.";

    const selectedIds = lignes.map((line) => String(line.medicamentId || "")).filter(Boolean);
    const uniqueCount = new Set(selectedIds).size;
    if (selectedIds.length !== uniqueCount) {
      return "Chaque médicament doit apparaître une seule fois dans la vente.";
    }

    for (const line of lignes) {
      const medicament = getMedicamentById(medicaments, line.medicamentId);
      if (!medicament) return "Sélectionnez un médicament valide pour chaque ligne.";
      if (!line.quantite || Number(line.quantite) <= 0) return "La quantité doit être supérieure à 0.";
      if (Number(line.quantite) > Number(medicament.stock_actuel)) {
        return `Stock insuffisant pour ${medicament.nom}. Disponible: ${medicament.stock_actuel}.`;
      }
    }

    return null;
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const validationError = validate();
    if (validationError) {
      setError(validationError);
      return;
    }

    setError(null);
    await onSubmit({
      notes,
      lignes: lignes.map((line) => ({
        medicament: Number(line.medicamentId),
        quantite: Number(line.quantite),
      })),
    });

    setNotes("");
    setLignes([{ medicamentId: "", quantite: 1 }]);
  };

  return (
    <form className="card form-grid" onSubmit={handleSubmit}>
      <h3>Nouvelle vente</h3>

      {lignes.map((line, index) => {
        const medicament = getMedicamentById(medicaments, line.medicamentId);
        const lineTotal = computeLineTotal(line);
        return (
          <div className="sale-line" key={`${index}-${line.medicamentId}`}>
            <select
              value={line.medicamentId}
              onChange={(event) => updateLine(index, "medicamentId", event.target.value)}
              required
            >
              <option value="">Sélectionner un médicament</option>
              {medicaments.map((item) => (
                <option key={item.id} value={item.id}>
                  {item.nom} — stock {item.stock_actuel}
                </option>
              ))}
            </select>

            <input
              type="number"
              min="1"
              value={line.quantite}
              onChange={(event) => updateLine(index, "quantite", event.target.value)}
              required
            />

            <div className="sale-line-meta">
              <span>PU: {medicament ? medicament.prix_vente : "0.00"}</span>
              <span>Total ligne: {lineTotal.toFixed(2)}</span>
            </div>

            <button type="button" className="btn-danger" onClick={() => removeLine(index)} disabled={lignes.length === 1}>
              Retirer
            </button>
          </div>
        );
      })}

      <button type="button" className="btn-secondary" onClick={addLine}>
        Ajouter une ligne
      </button>

      <textarea
        className="notes-textarea"
        value={notes}
        onChange={(event) => setNotes(event.target.value)}
        placeholder="Notes optionnelles"
      />

      <div className="sale-total">Total estimé: {total.toFixed(2)}</div>

      {error ? <div className="status-banner status-error">{error}</div> : null}

      <div className="form-actions">
        <button type="submit" disabled={submitting}>
          {submitting ? "Enregistrement..." : "Créer la vente"}
        </button>
      </div>
    </form>
  );
};

export default VenteForm;