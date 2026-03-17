"""Models for ventes app."""
from decimal import Decimal

from django.db import models
from django.utils import timezone


class Vente(models.Model):
	"""Represents a sale transaction in the pharmacy."""

	class Statut(models.TextChoices):
		"""Possible lifecycle states for a sale."""

		EN_COURS = "EN_COURS", "En cours"
		COMPLETEE = "COMPLETEE", "Complétée"
		ANNULEE = "ANNULEE", "Annulée"

	reference = models.CharField(max_length=20, unique=True, blank=True)
	date_vente = models.DateTimeField(default=timezone.now)
	total_ttc = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))
	statut = models.CharField(max_length=20, choices=Statut.choices, default=Statut.COMPLETEE)
	notes = models.TextField(blank=True, null=True)
	est_active = models.BooleanField(default=True)

	class Meta:
		ordering = ["-date_vente", "-id"]
		verbose_name = "Vente"
		verbose_name_plural = "Ventes"

	def __str__(self) -> str:
		"""Return a readable representation for admin and logs."""
		return self.reference or f"Vente #{self.pk}"

	def save(self, *args, **kwargs):
		"""Generate a stable business reference after first persistence."""
		is_creation = self.pk is None
		super().save(*args, **kwargs)

		if is_creation and not self.reference:
			year = self.date_vente.year if self.date_vente else timezone.now().year
			self.reference = f"VNT-{year}-{self.pk:04d}"
			super().save(update_fields=["reference"])


class LigneVente(models.Model):
	"""Represents one medicament line inside a sale."""

	vente = models.ForeignKey(Vente, on_delete=models.CASCADE, related_name="lignes")
	medicament = models.ForeignKey("medicaments.Medicament", on_delete=models.PROTECT, related_name="lignes_vente")
	quantite = models.PositiveIntegerField()
	prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
	sous_total = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))

	class Meta:
		verbose_name = "Ligne de vente"
		verbose_name_plural = "Lignes de vente"

	def __str__(self) -> str:
		"""Return a readable representation for one sale line."""
		return f"{self.medicament.nom} x {self.quantite}"

	def save(self, *args, **kwargs):
		"""Calculate subtotal before persistence."""
		self.sous_total = Decimal(self.quantite) * self.prix_unitaire
		super().save(*args, **kwargs)
