"""API tests for categories endpoints."""
from rest_framework import status
from rest_framework.test import APITestCase

from apps.categories.models import Categorie


class CategoriesApiTests(APITestCase):
    """Validate category CRUD endpoints."""

    def test_create_and_list_categories(self):
        """Should create category then return it in list endpoint."""
        create_response = self.client.post("/api/v1/categories/", {"nom": "Antibiotique"}, format="json")
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        list_response = self.client.get("/api/v1/categories/")
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(list_response.data["count"], 1)

    def test_delete_category_returns_204(self):
        """Delete endpoint should return HTTP 204 for existing category."""
        categorie = Categorie.objects.create(nom="Dermatologie")
        delete_response = self.client.delete(f"/api/v1/categories/{categorie.id}/")
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
