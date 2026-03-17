"""Model tests for medicaments app."""
from datetime import date, timedelta

from django.test import TestCase

from apps.categories.models import Categorie
from apps.medicaments.models import Medicament


class MedicamentModelTests(TestCase):
    """Validate medicament model computed properties."""

    def test_est_en_alerte_property(self):
        """`est_en_alerte` should be true when stock is below threshold."""
        categorie = Categorie.objects.create(nom="Antalgique")
        medicament = Medicament.objects.create(
            nom="Doliprane",
            dci="Paracetamol",
            categorie=categorie,
            forme="Comprimé",
            dosage="500mg",
            prix_achat="5.00",
            prix_vente="7.00",
            stock_actuel=2,
            stock_minimum=5,
            date_expiration=date.today() + timedelta(days=365),
        )
        self.assertTrue(medicament.est_en_alerte)
