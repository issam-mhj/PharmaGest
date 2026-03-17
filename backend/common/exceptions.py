"""Shared API exception handling for PharmaManager."""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


ERROR_CODE_BY_STATUS = {
    status.HTTP_400_BAD_REQUEST: "validation_error",
    status.HTTP_401_UNAUTHORIZED: "unauthorized",
    status.HTTP_403_FORBIDDEN: "forbidden",
    status.HTTP_404_NOT_FOUND: "not_found",
    status.HTTP_422_UNPROCESSABLE_ENTITY: "unprocessable_entity",
}


def custom_exception_handler(exc, context):
    """Return a normalized JSON payload for handled DRF exceptions."""
    response = exception_handler(exc, context)

    if response is None:
        return Response(
            {
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "error": "server_error",
                "detail": "Une erreur interne est survenue.",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    detail = response.data
    if isinstance(detail, dict) and "detail" in detail:
        message = detail["detail"]
    else:
        message = detail

    response.data = {
        "status_code": response.status_code,
        "error": ERROR_CODE_BY_STATUS.get(response.status_code, "api_error"),
        "detail": message,
    }
    return response