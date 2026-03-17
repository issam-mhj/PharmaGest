"""Model tests for categories app."""
from django.test import TestCase

from apps.categories.models import Categorie


class CategorieModelTests(TestCase):
    """Validate core category model behavior."""

    def test_str_returns_nom(self):
        """`__str__` should return category name."""
        categorie = Categorie.objects.create(nom="Antalgique")
        self.assertEqual(str(categorie), "Antalgique")
