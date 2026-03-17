"""Model tests for ventes app."""
from datetime import date, timedelta

from django.test import TestCase

from apps.categories.models import Categorie
from apps.medicaments.models import Medicament
from apps.ventes.models import LigneVente, Vente


class VenteModelTests(TestCase):
    """Validate sale model fields and computed values."""

    def setUp(self):
        categorie = Categorie.objects.create(nom="Test")
        self.medicament = Medicament.objects.create(
            nom="TestMed",
            dci="TestMed",
            categorie=categorie,
            forme="Comprimé",
            dosage="10mg",
            prix_achat="2.00",
            prix_vente="3.50",
            stock_actuel=100,
            stock_minimum=5,
            date_expiration=date.today() + timedelta(days=365),
            ordonnance_requise=False,
        )

    def test_reference_generated_on_save(self):
        """Sale save should auto-generate business reference."""
        vente = Vente.objects.create(notes="Test")
        self.assertTrue(vente.reference.startswith("VNT-"))

    def test_ligne_sous_total_is_calculated(self):
        """Sale line should compute subtotal from quantity and unit price."""
        vente = Vente.objects.create(notes="Test")
        ligne = LigneVente.objects.create(
            vente=vente,
            medicament=self.medicament,
            quantite=3,
            prix_unitaire="3.50",
        )
        self.assertEqual(str(ligne.sous_total), "10.50")
