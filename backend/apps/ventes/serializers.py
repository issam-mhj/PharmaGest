"""Serializers for ventes app."""
from rest_framework import serializers

from .models import LigneVente, Vente
from .services import create_vente_with_stock_deduction


class LigneVenteReadSerializer(serializers.ModelSerializer):
	"""Read serializer for sale lines."""

	medicament_nom = serializers.CharField(source="medicament.nom", read_only=True)

	class Meta:
		model = LigneVente
		fields = ["id", "medicament", "medicament_nom", "quantite", "prix_unitaire", "sous_total"]
		read_only_fields = fields


class LigneVenteWriteSerializer(serializers.Serializer):
	"""Write serializer for line payload during sale creation."""

	medicament = serializers.IntegerField()
	quantite = serializers.IntegerField(min_value=1)


class VenteSerializer(serializers.ModelSerializer):
	"""Serializer for sale read operations."""

	lignes = LigneVenteReadSerializer(many=True, read_only=True)

	class Meta:
		model = Vente
		fields = [
			"id",
			"reference",
			"date_vente",
			"total_ttc",
			"statut",
			"notes",
			"est_active",
			"lignes",
		]
		read_only_fields = fields


class VenteCreateSerializer(serializers.Serializer):
	"""Serializer for sale creation with nested line payload."""

	notes = serializers.CharField(required=False, allow_blank=True, allow_null=True)
	lignes = LigneVenteWriteSerializer(many=True)

	def validate_lignes(self, value):
		"""Ensure at least one sale line exists."""
		if not value:
			raise serializers.ValidationError("La vente doit contenir au moins une ligne.")
		return value

	def create(self, validated_data):
		"""Delegate transactional creation to dedicated service layer."""
		return create_vente_with_stock_deduction(
			notes=validated_data.get("notes"),
			lignes_data=validated_data.get("lignes", []),
		)
