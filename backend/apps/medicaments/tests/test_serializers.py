"""Serializer tests for medicaments app."""
from datetime import date, timedelta

from django.test import TestCase

from apps.categories.models import Categorie
from apps.medicaments.serializers import MedicamentSerializer


class MedicamentSerializerTests(TestCase):
    """Validate medicament serializer business rules."""

    def setUp(self):
        self.categorie = Categorie.objects.create(nom="Antibiotique")

    def test_reject_when_selling_price_lower_than_purchase_price(self):
        """Serializer should reject payload where `prix_vente` < `prix_achat`."""
        payload = {
            "nom": "Amoxicilline",
            "dci": "Amoxicilline",
            "categorie": self.categorie.id,
            "forme": "Comprimé",
            "dosage": "500mg",
            "prix_achat": "12.00",
            "prix_vente": "10.00",
            "stock_actuel": 10,
            "stock_minimum": 2,
            "date_expiration": date.today() + timedelta(days=365),
            "ordonnance_requise": True,
        }
        serializer = MedicamentSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertIn("prix_vente", serializer.errors)
