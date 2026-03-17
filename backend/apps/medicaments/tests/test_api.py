"""API tests for medicaments endpoints."""
from datetime import date, timedelta

from rest_framework import status
from rest_framework.test import APITestCase

from apps.categories.models import Categorie
from apps.medicaments.models import Medicament


class MedicamentsApiTests(APITestCase):
    """Validate medicament CRUD/alerts/soft-delete endpoints."""

    def setUp(self):
        self.categorie = Categorie.objects.create(nom="Antalgique")
        self.medicament = Medicament.objects.create(
            nom="Ibuprofene",
            dci="Ibuprofene",
            categorie=self.categorie,
            forme="Comprimé",
            dosage="400mg",
            prix_achat="6.00",
            prix_vente="9.50",
            stock_actuel=3,
            stock_minimum=5,
            date_expiration=date.today() + timedelta(days=365),
            ordonnance_requise=False,
        )

    def test_alertes_returns_low_stock_medicaments(self):
        """Alerts endpoint should include medicaments below minimum stock."""
        response = self.client.get("/api/v1/medicaments/alertes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_applies_soft_delete(self):
        """Delete endpoint should archive medicament without hard deletion."""
        response = self.client.delete(f"/api/v1/medicaments/{self.medicament.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.medicament.refresh_from_db()
        self.assertFalse(self.medicament.est_actif)
