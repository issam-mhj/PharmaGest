"""Admin registration for medicaments app."""
from django.contrib import admin

from .models import Medicament


@admin.register(Medicament)
class MedicamentAdmin(admin.ModelAdmin):
	"""Admin settings for medicament management."""

	list_display = (
		"id",
		"nom",
		"categorie",
		"prix_vente",
		"stock_actuel",
		"stock_minimum",
		"date_expiration",
		"est_actif",
	)
	list_filter = ("categorie", "ordonnance_requise", "est_actif")
	search_fields = ("nom", "dci", "forme", "dosage")
	ordering = ("nom",)
