"""Serializer tests for categories app."""
from django.test import TestCase

from apps.categories.models import Categorie
from apps.categories.serializers import CategorieSerializer


class CategorieSerializerTests(TestCase):
    """Validate category serializer business rules."""

    def test_nom_must_be_unique_case_insensitive(self):
        """Serializer should reject names matching existing category ignoring case."""
        Categorie.objects.create(nom="Antibiotique")
        serializer = CategorieSerializer(data={"nom": "antibiotique"})
        self.assertFalse(serializer.is_valid())
        self.assertIn("nom", serializer.errors)
