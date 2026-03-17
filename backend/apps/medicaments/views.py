"""Views for medicaments app."""
from django.db.models import F
from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema, extend_schema_view
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Medicament
from .serializers import MedicamentSerializer


@extend_schema_view(
	list=extend_schema(
		tags=["Medicaments"],
		summary="Lister les médicaments actifs",
		description="Retourne la liste paginée des médicaments actifs avec recherche et filtres.",
		responses={status.HTTP_200_OK: OpenApiResponse(description="Liste des médicaments récupérée.")},
	),
	retrieve=extend_schema(
		tags=["Medicaments"],
		summary="Détail d'un médicament",
		description="Retourne le détail d'un médicament actif.",
		responses={
			status.HTTP_200_OK: OpenApiResponse(description="Médicament trouvé."),
			status.HTTP_404_NOT_FOUND: OpenApiResponse(description="Médicament introuvable."),
		},
	),
	create=extend_schema(
		tags=["Medicaments"],
		summary="Créer un médicament",
		description="Crée un nouveau médicament dans le catalogue actif.",
		examples=[
			OpenApiExample(
				"Exemple création médicament",
				value={
					"nom": "Amoxicilline",
					"dci": "Amoxicilline",
					"categorie": 1,
					"forme": "Comprimé",
					"dosage": "500mg",
					"prix_achat": "8.00",
					"prix_vente": "12.50",
					"stock_actuel": 80,
					"stock_minimum": 15,
					"date_expiration": "2027-09-30",
					"ordonnance_requise": True,
				},
				request_only=True,
			)
		],
		responses={
			status.HTTP_201_CREATED: OpenApiResponse(description="Médicament créé avec succès."),
			status.HTTP_400_BAD_REQUEST: OpenApiResponse(description="Données invalides."),
		},
	),
	update=extend_schema(
		tags=["Medicaments"],
		summary="Modifier un médicament",
		description="Met à jour entièrement un médicament actif.",
		responses={
			status.HTTP_200_OK: OpenApiResponse(description="Médicament mis à jour."),
			status.HTTP_400_BAD_REQUEST: OpenApiResponse(description="Données invalides."),
			status.HTTP_404_NOT_FOUND: OpenApiResponse(description="Médicament introuvable."),
		},
	),
	partial_update=extend_schema(
		tags=["Medicaments"],
		summary="Mettre à jour partiellement un médicament",
		description="Met à jour partiellement un médicament actif.",
		responses={
			status.HTTP_200_OK: OpenApiResponse(description="Médicament mis à jour partiellement."),
			status.HTTP_400_BAD_REQUEST: OpenApiResponse(description="Données invalides."),
			status.HTTP_404_NOT_FOUND: OpenApiResponse(description="Médicament introuvable."),
		},
	),
	destroy=extend_schema(
		tags=["Medicaments"],
		summary="Archiver un médicament (soft delete)",
		description="Désactive le médicament en passant `est_actif` à `False`.",
		responses={
			status.HTTP_204_NO_CONTENT: OpenApiResponse(description="Médicament archivé avec succès."),
			status.HTTP_404_NOT_FOUND: OpenApiResponse(description="Médicament introuvable."),
		},
	),
)
class MedicamentViewSet(viewsets.ModelViewSet):
	"""CRUD viewset for active medicaments with soft delete behavior."""

	serializer_class = MedicamentSerializer
	permission_classes = [AllowAny]
	filterset_fields = ["categorie", "ordonnance_requise", "est_actif", "date_expiration"]
	search_fields = ["nom", "dci", "forme", "dosage"]
	ordering_fields = ["nom", "prix_vente", "stock_actuel", "date_expiration", "date_creation"]

	def get_queryset(self):
		"""Return active medicaments by default."""
		return Medicament.objects.filter(est_actif=True).select_related("categorie")

	def perform_destroy(self, instance):
		"""Apply soft delete by disabling medicament instead of deleting row."""
		instance.est_actif = False
		instance.save(update_fields=["est_actif"])

	@extend_schema(
		tags=["Medicaments"],
		summary="Lister les alertes de stock",
		description="Retourne les médicaments actifs dont le stock est inférieur ou égal au seuil minimum.",
		responses={status.HTTP_200_OK: MedicamentSerializer(many=True)},
	)
	@action(detail=False, methods=["get"], url_path="alertes")
	def alertes(self, request):
		"""Return active medicaments where stock is under alert threshold."""
		queryset = self.get_queryset().filter(stock_actuel__lte=F("stock_minimum")).order_by("stock_actuel", "nom")
		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
