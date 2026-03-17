"""Views for categories app."""
from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema, extend_schema_view
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny

from .models import Categorie
from .serializers import CategorieSerializer


@extend_schema_view(
	list=extend_schema(
		tags=["Categories"],
		summary="Lister les catégories",
		description="Retourne la liste paginée des catégories triées par nom.",
		responses={
			status.HTTP_200_OK: OpenApiResponse(description="Liste des catégories récupérée avec succès."),
		},
	),
	retrieve=extend_schema(
		tags=["Categories"],
		summary="Détail d'une catégorie",
		description="Retourne le détail d'une catégorie spécifique.",
		responses={
			status.HTTP_200_OK: OpenApiResponse(description="Catégorie trouvée."),
			status.HTTP_404_NOT_FOUND: OpenApiResponse(description="Catégorie introuvable."),
		},
	),
	create=extend_schema(
		tags=["Categories"],
		summary="Créer une catégorie",
		description="Crée une nouvelle catégorie de médicaments.",
		examples=[
			OpenApiExample(
				"Exemple de création",
				value={
					"nom": "Antibiotique",
					"description": "Médicaments destinés aux infections bactériennes.",
				},
				request_only=True,
			)
		],
		responses={
			status.HTTP_201_CREATED: OpenApiResponse(description="Catégorie créée avec succès."),
			status.HTTP_400_BAD_REQUEST: OpenApiResponse(description="Données invalides."),
		},
	),
	update=extend_schema(
		tags=["Categories"],
		summary="Modifier une catégorie",
		description="Met à jour entièrement une catégorie existante.",
		responses={
			status.HTTP_200_OK: OpenApiResponse(description="Catégorie mise à jour avec succès."),
			status.HTTP_400_BAD_REQUEST: OpenApiResponse(description="Données invalides."),
			status.HTTP_404_NOT_FOUND: OpenApiResponse(description="Catégorie introuvable."),
		},
	),
	partial_update=extend_schema(
		tags=["Categories"],
		summary="Mettre à jour partiellement une catégorie",
		description="Met à jour partiellement une catégorie existante.",
		responses={
			status.HTTP_200_OK: OpenApiResponse(description="Catégorie mise à jour partiellement."),
			status.HTTP_400_BAD_REQUEST: OpenApiResponse(description="Données invalides."),
			status.HTTP_404_NOT_FOUND: OpenApiResponse(description="Catégorie introuvable."),
		},
	),
	destroy=extend_schema(
		tags=["Categories"],
		summary="Supprimer une catégorie",
		description="Supprime une catégorie si elle n'est pas liée à des médicaments protégés.",
		responses={
			status.HTTP_204_NO_CONTENT: OpenApiResponse(description="Catégorie supprimée avec succès."),
			status.HTTP_404_NOT_FOUND: OpenApiResponse(description="Catégorie introuvable."),
		},
	),
)
class CategorieViewSet(viewsets.ModelViewSet):
	"""CRUD viewset for medicine categories."""

	queryset = Categorie.objects.all().order_by("nom")
	serializer_class = CategorieSerializer
	permission_classes = [AllowAny]
	search_fields = ["nom", "description"]
	ordering_fields = ["nom", "date_creation", "date_modification"]
