"""Filtering tools for sale history endpoints."""
import django_filters

from .models import Vente


class VenteFilter(django_filters.FilterSet):
    """Filter sales by status and sale date interval."""

    date_vente_debut = django_filters.DateFilter(field_name="date_vente", lookup_expr="date__gte")
    date_vente_fin = django_filters.DateFilter(field_name="date_vente", lookup_expr="date__lte")

    class Meta:
        model = Vente
        fields = ["statut", "date_vente_debut", "date_vente_fin"]