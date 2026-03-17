"""Admin registration for ventes app."""
from django.contrib import admin

from .models import LigneVente, Vente


class LigneVenteInline(admin.TabularInline):
	"""Inline display for sale lines inside sale admin."""

	model = LigneVente
	extra = 0
	readonly_fields = ("sous_total",)


@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
	"""Admin configuration for sales."""

	list_display = ("id", "reference", "date_vente", "total_ttc", "statut", "est_active")
	list_filter = ("statut", "est_active", "date_vente")
	search_fields = ("reference", "notes")
	ordering = ("-date_vente",)
	inlines = [LigneVenteInline]


@admin.register(LigneVente)
class LigneVenteAdmin(admin.ModelAdmin):
	"""Admin configuration for sale lines."""

	list_display = ("id", "vente", "medicament", "quantite", "prix_unitaire", "sous_total")
	list_select_related = ("vente", "medicament")
