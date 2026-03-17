"""Serializer tests for ventes app."""
from datetime import date, timedelta

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from apps.categories.models import Categorie
from apps.medicaments.models import Medicament
from apps.ventes.serializers import VenteCreateSerializer


class VenteCreateSerializerTests(TestCase):
    """Validate sale creation serializer behavior."""

    def setUp(self):
        categorie = Categorie.objects.create(nom="Cardio")
        self.medicament = Medicament.objects.create(
            nom="Aspirine",
            dci="Acide acetylsalicylique",
            categorie=categorie,
            forme="Comprimé",
            dosage="100mg",
            prix_achat="2.50",
            prix_vente="4.00",
            stock_actuel=5,
            stock_minimum=2,
            date_expiration=date.today() + timedelta(days=365),
            ordonnance_requise=False,
        )

    def test_reject_sale_when_stock_insufficient(self):
        """Should return invalid serializer when requested quantity exceeds stock."""
        serializer = VenteCreateSerializer(
            data={"lignes": [{"medicament": self.medicament.id, "quantite": 999}]}
        )
        self.assertTrue(serializer.is_valid())
        with self.assertRaises(ValidationError):
            serializer.save()
