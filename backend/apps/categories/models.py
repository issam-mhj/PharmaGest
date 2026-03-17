"""Models for categories app."""
from django.db import models


class Categorie(models.Model):
	"""Represents a medicine category used to classify medicaments."""

	nom = models.CharField(max_length=120, unique=True)
	description = models.TextField(blank=True, null=True)
	date_creation = models.DateTimeField(auto_now_add=True)
	date_modification = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["nom"]
		verbose_name = "Catégorie"
		verbose_name_plural = "Catégories"

	def __str__(self) -> str:
		"""Return a readable string representation for admin and logs."""
		return self.nom
