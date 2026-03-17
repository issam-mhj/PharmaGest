"""Models for medicaments app."""
from django.db import models


class Medicament(models.Model):
	"""Represents a medicament managed by the pharmacy inventory."""

	nom = models.CharField(max_length=200)
	dci = models.CharField(max_length=200)
	categorie = models.ForeignKey(
		"categories.Categorie",
		on_delete=models.PROTECT,
		related_name="medicaments",
	)
	forme = models.CharField(max_length=120)
	dosage = models.CharField(max_length=120)
	prix_achat = models.DecimalField(max_digits=10, decimal_places=2)
	prix_vente = models.DecimalField(max_digits=10, decimal_places=2)
	stock_actuel = models.PositiveIntegerField(default=0)
	stock_minimum = models.PositiveIntegerField(default=10)
	date_expiration = models.DateField()
	ordonnance_requise = models.BooleanField(default=False)
	date_creation = models.DateTimeField(auto_now_add=True)
	est_actif = models.BooleanField(default=True)

	class Meta:
		ordering = ["nom"]
		verbose_name = "Médicament"
		verbose_name_plural = "Médicaments"

	def __str__(self) -> str:
		"""Return a readable representation of the medicament."""
		return f"{self.nom} ({self.dosage})"

	@property
	def est_en_alerte(self) -> bool:
		"""Return `True` when current stock is lower than or equal to alert threshold."""
		return self.stock_actuel <= self.stock_minimum
