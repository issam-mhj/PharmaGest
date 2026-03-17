"""Views for ventes app."""
from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema, extend_schema_view
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .filters import VenteFilter
from .models import Vente
from .serializers import VenteCreateSerializer, VenteSerializer
from .services import cancel_vente_and_restore_stock


@extend_schema_view(
	list=extend_schema(
		tags=["Ventes"],
		summary="Historique des ventes",
		description="Retourne l'historique paginé des ventes avec filtres date/statut.",
		responses={status.HTTP_200_OK: OpenApiResponse(description="Historique des ventes récupéré.")},
	),
	retrieve=extend_schema(
		tags=["Ventes"],
		summary="Détail d'une vente",
		description="Retourne le détail complet d'une vente avec ses lignes.",
		responses={
			status.HTTP_200_OK: OpenApiResponse(description="Vente trouvée."),
			status.HTTP_404_NOT_FOUND: OpenApiResponse(description="Vente introuvable."),
		},
	),
	create=extend_schema(
		tags=["Ventes"],
		summary="Créer une vente",
		description="Crée une vente avec ses lignes, snapshot des prix et déduction stock.",
		examples=[
			OpenApiExample(
				"Exemple création vente",
				value={
					"notes": "Client régulier",
					"lignes": [
						{"medicament": 1, "quantite": 2},
						{"medicament": 2, "quantite": 1},
					],
				},
				request_only=True,
			)
		],
		responses={
			status.HTTP_201_CREATED: OpenApiResponse(description="Vente créée avec succès."),
			status.HTTP_400_BAD_REQUEST: OpenApiResponse(description="Données invalides."),
		},
	),
)
class VenteViewSet(viewsets.ModelViewSet):
	"""Viewset exposing sale history, creation, and cancellation workflow."""

	queryset = Vente.objects.prefetch_related("lignes__medicament").all()
	permission_classes = [AllowAny]
	filterset_class = VenteFilter
	search_fields = ["reference", "notes"]
	ordering_fields = ["date_vente", "total_ttc", "reference"]
	http_method_names = ["get", "post", "head", "options"]

	def get_serializer_class(self):
		"""Use a dedicated serializer for create requests."""
		if self.action == "create":
			return VenteCreateSerializer
		return VenteSerializer

	def create(self, request, *args, **kwargs):
		"""Create a sale then return normalized read representation."""
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		vente = serializer.save()
		read_serializer = VenteSerializer(instance=vente, context={"request": request})
		return Response(read_serializer.data, status=status.HTTP_201_CREATED)

	@extend_schema(
		tags=["Ventes"],
		summary="Annuler une vente",
		description="Annule une vente, réintègre automatiquement les stocks et désactive la vente.",
		responses={
			status.HTTP_200_OK: VenteSerializer,
			status.HTTP_400_BAD_REQUEST: OpenApiResponse(description="Vente déjà annulée ou invalide."),
			status.HTTP_404_NOT_FOUND: OpenApiResponse(description="Vente introuvable."),
		},
	)
	@action(detail=True, methods=["post"], url_path="annuler")
	def annuler(self, request, pk=None):
		"""Cancel a sale and restore stock levels atomically."""
		vente = self.get_object()
		vente = cancel_vente_and_restore_stock(vente)
		serializer = VenteSerializer(instance=vente, context={"request": request})
		return Response(serializer.data, status=status.HTTP_200_OK)
