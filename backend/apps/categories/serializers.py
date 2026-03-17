"""Serializers for categories app."""
from rest_framework import serializers

from .models import Categorie


class CategorieSerializer(serializers.ModelSerializer):
	"""Serializer for category read/write operations with business validations."""

	class Meta:
		model = Categorie
		fields = [
			"id",
			"nom",
			"description",
			"date_creation",
			"date_modification",
		]
		read_only_fields = ["id", "date_creation", "date_modification"]

	def validate_nom(self, value: str) -> str:
		"""Ensure `nom` is not empty and remains unique in a case-insensitive way."""
		cleaned_value = value.strip()
		if not cleaned_value:
			raise serializers.ValidationError("Le nom de la catégorie est obligatoire.")

		queryset = Categorie.objects.filter(nom__iexact=cleaned_value)
		if self.instance:
			queryset = queryset.exclude(pk=self.instance.pk)

		if queryset.exists():
			raise serializers.ValidationError("Une catégorie avec ce nom existe déjà.")

		return cleaned_value
