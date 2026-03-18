"""Authentication endpoints for JWT flows."""
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class CurrentUserView(APIView):
    """Return profile information for the authenticated user."""

    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        tags=["Auth"],
        summary="Profil utilisateur courant",
        description="Retourne les informations du compte connecté via JWT.",
        responses={
            status.HTTP_200_OK: OpenApiResponse(description="Profil utilisateur récupéré."),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(description="Token manquant ou invalide."),
        },
    )
    def get(self, request):
        """Return current authenticated user payload."""
        user = request.user
        return Response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "is_staff": user.is_staff,
            },
            status=status.HTTP_200_OK,
        )
