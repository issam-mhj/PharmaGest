"""Serializers for medicaments app."""
from datetime import date
from decimal import Decimal

from rest_framework import serializers

from .models import Medicament


class MedicamentSerializer(serializers.ModelSerializer):
	"""Serializer handling medicament CRUD and business validations."""

	est_en_alerte = serializers.BooleanField(read_only=True)

	class Meta:
		model = Medicament
		fields = [
			"id",
			"nom",
			"dci",
			"categorie",
			"forme",
			"dosage",
			"prix_achat",
			"prix_vente",
			"stock_actuel",
			"stock_minimum",
			"date_expiration",
			"ordonnance_requise",
			"date_creation",
			"est_actif",
			"est_en_alerte",
		]
		read_only_fields = ["id", "date_creation", "est_actif", "est_en_alerte"]

	def validate_nom(self, value: str) -> str:
		"""Ensure `nom` is present and normalized."""
		cleaned_value = value.strip()
		if not cleaned_value:
			raise serializers.ValidationError("Le nom du médicament est obligatoire.")
		return cleaned_value

	def validate_dci(self, value: str) -> str:
		"""Ensure `dci` is present and normalized."""
		cleaned_value = value.strip()
		if not cleaned_value:
			raise serializers.ValidationError("La DCI est obligatoire.")
		return cleaned_value

	def validate_forme(self, value: str) -> str:
		"""Ensure `forme` is present and normalized."""
		cleaned_value = value.strip()
		if not cleaned_value:
			raise serializers.ValidationError("La forme galénique est obligatoire.")
		return cleaned_value

	def validate_dosage(self, value: str) -> str:
		"""Ensure `dosage` is present and normalized."""
		cleaned_value = value.strip()
		if not cleaned_value:
			raise serializers.ValidationError("Le dosage est obligatoire.")
		return cleaned_value

	def validate_prix_achat(self, value: Decimal) -> Decimal:
		"""Ensure purchase price is strictly positive."""
		if value <= 0:
			raise serializers.ValidationError("Le prix d'achat doit être supérieur à 0.")
		return value

	def validate_prix_vente(self, value: Decimal) -> Decimal:
		"""Ensure selling price is strictly positive."""
		if value <= 0:
			raise serializers.ValidationError("Le prix de vente doit être supérieur à 0.")
		return value

	def validate_date_expiration(self, value):
		"""Ensure expiration date is valid and not in the past."""
		if value < date.today():
			raise serializers.ValidationError("La date d'expiration ne peut pas être dans le passé.")
		return value

	def validate(self, attrs):
		"""Cross-field business validations."""
		prix_achat = attrs.get("prix_achat", getattr(self.instance, "prix_achat", None))
		prix_vente = attrs.get("prix_vente", getattr(self.instance, "prix_vente", None))
		stock_actuel = attrs.get("stock_actuel", getattr(self.instance, "stock_actuel", 0))
		stock_minimum = attrs.get("stock_minimum", getattr(self.instance, "stock_minimum", 0))

		if prix_achat is not None and prix_vente is not None and prix_vente < prix_achat:
			raise serializers.ValidationError(
				{"prix_vente": "Le prix de vente doit être supérieur ou égal au prix d'achat."}
			)

		if stock_actuel is not None and stock_actuel < 0:
			raise serializers.ValidationError({"stock_actuel": "Le stock actuel ne peut pas être négatif."})

		if stock_minimum is not None and stock_minimum < 0:
			raise serializers.ValidationError({"stock_minimum": "Le stock minimum ne peut pas être négatif."})

		return attrs
