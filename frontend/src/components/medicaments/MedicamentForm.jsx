import React, { useEffect, useState } from "react";

const initialForm = {
  nom: "",
  dci: "",
  categorie: "",
  forme: "",
  dosage: "",
  prix_achat: "",
  prix_vente: "",
  stock_actuel: "0",
  stock_minimum: "10",
  date_expiration: "",
  ordonnance_requise: false,
};

const MedicamentForm = ({ categories, selectedMedicament, onSubmit, onCancel, submitting }) => {
  const [formData, setFormData] = useState(initialForm);

  useEffect(() => {
    if (!selectedMedicament) {
      setFormData(initialForm);
      return;
    }

    setFormData({
      nom: selectedMedicament.nom || "",
      dci: selectedMedicament.dci || "",
      categorie: String(selectedMedicament.categorie || ""),
      forme: selectedMedicament.forme || "",
      dosage: selectedMedicament.dosage || "",
      prix_achat: String(selectedMedicament.prix_achat || ""),
      prix_vente: String(selectedMedicament.prix_vente || ""),
      stock_actuel: String(selectedMedicament.stock_actuel || "0"),
      stock_minimum: String(selectedMedicament.stock_minimum || "10"),
      date_expiration: selectedMedicament.date_expiration || "",
      ordonnance_requise: Boolean(selectedMedicament.ordonnance_requise),
    });
  }, [selectedMedicament]);

  const handleChange = (key, value) => {
    setFormData((current) => ({ ...current, [key]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    onSubmit({
      ...formData,
      categorie: Number(formData.categorie),
      prix_achat: Number(formData.prix_achat),
      prix_vente: Number(formData.prix_vente),
      stock_actuel: Number(formData.stock_actuel),
      stock_minimum: Number(formData.stock_minimum),
    });
  };

  return (
    <form className="card form-grid" onSubmit={handleSubmit}>
      <h3>{selectedMedicament ? "Modifier un médicament" : "Ajouter un médicament"}</h3>

      <input placeholder="Nom commercial" value={formData.nom} onChange={(e) => handleChange("nom", e.target.value)} required />
      <input placeholder="DCI" value={formData.dci} onChange={(e) => handleChange("dci", e.target.value)} required />

      <select value={formData.categorie} onChange={(e) => handleChange("categorie", e.target.value)} required>
        <option value="">Sélectionner une catégorie</option>
        {categories.map((category) => (
          <option key={category.id} value={category.id}>
            {category.nom}
          </option>
        ))}
      </select>

      <input placeholder="Forme" value={formData.forme} onChange={(e) => handleChange("forme", e.target.value)} required />
      <input placeholder="Dosage" value={formData.dosage} onChange={(e) => handleChange("dosage", e.target.value)} required />

      <input type="number" step="0.01" placeholder="Prix achat" value={formData.prix_achat} onChange={(e) => handleChange("prix_achat", e.target.value)} required />
      <input type="number" step="0.01" placeholder="Prix vente" value={formData.prix_vente} onChange={(e) => handleChange("prix_vente", e.target.value)} required />

      <input type="number" placeholder="Stock actuel" value={formData.stock_actuel} onChange={(e) => handleChange("stock_actuel", e.target.value)} required />
      <input type="number" placeholder="Stock minimum" value={formData.stock_minimum} onChange={(e) => handleChange("stock_minimum", e.target.value)} required />

      <input type="date" value={formData.date_expiration} onChange={(e) => handleChange("date_expiration", e.target.value)} required />

      <label className="checkbox-line">
        <input
          type="checkbox"
          checked={formData.ordonnance_requise}
          onChange={(e) => handleChange("ordonnance_requise", e.target.checked)}
        />
        Ordonnance requise
      </label>

      <div className="form-actions">
        <button type="submit" disabled={submitting}>
          {submitting ? "Enregistrement..." : selectedMedicament ? "Mettre à jour" : "Créer"}
        </button>
        {selectedMedicament ? (
          <button type="button" className="btn-secondary" onClick={onCancel}>
            Annuler l’édition
          </button>
        ) : null}
      </div>
    </form>
  );
};

export default MedicamentForm;