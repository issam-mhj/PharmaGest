"""API tests for ventes endpoints."""
from datetime import date, timedelta

from rest_framework import status
from rest_framework.test import APITestCase

from apps.categories.models import Categorie
from apps.medicaments.models import Medicament


class VentesApiTests(APITestCase):
    """Validate sales creation/history/cancel endpoints."""

    def setUp(self):
        categorie = Categorie.objects.create(nom="Antibiotique")
        self.medicament = Medicament.objects.create(
            nom="Azithromycine",
            dci="Azithromycine",
            categorie=categorie,
            forme="Comprimé",
            dosage="500mg",
            prix_achat="10.00",
            prix_vente="15.00",
            stock_actuel=20,
            stock_minimum=5,
            date_expiration=date.today() + timedelta(days=365),
            ordonnance_requise=True,
        )

    def test_create_sale_deducts_stock(self):
        """Creating sale should deduct stock and return 201."""
        payload = {"notes": "Test", "lignes": [{"medicament": self.medicament.id, "quantite": 3}]}
        response = self.client.post("/api/v1/ventes/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.medicament.refresh_from_db()
        self.assertEqual(self.medicament.stock_actuel, 17)

    def test_cancel_sale_restores_stock(self):
        """Cancel endpoint should restore stock and mark sale as cancelled."""
        create_payload = {"notes": "Cancel test", "lignes": [{"medicament": self.medicament.id, "quantite": 4}]}
        create_response = self.client.post("/api/v1/ventes/", create_payload, format="json")
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        vente_id = create_response.data["id"]
        cancel_response = self.client.post(f"/api/v1/ventes/{vente_id}/annuler/", {}, format="json")
        self.assertEqual(cancel_response.status_code, status.HTTP_200_OK)

        self.medicament.refresh_from_db()
        self.assertEqual(self.medicament.stock_actuel, 20)

    def test_create_sale_with_insufficient_stock_returns_400(self):
        """Sale creation should fail with HTTP 400 when stock is insufficient."""
        payload = {"lignes": [{"medicament": self.medicament.id, "quantite": 999}]}
        response = self.client.post("/api/v1/ventes/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"], "validation_error")
