"""Admin registration for categories app."""
from django.contrib import admin

from .models import Categorie


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
	"""Admin configuration for category management."""

	list_display = ("id", "nom", "date_creation", "date_modification")
	search_fields = ("nom", "description")
	ordering = ("nom",)
