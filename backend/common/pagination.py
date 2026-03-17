"""Shared pagination classes for PharmaManager API."""
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """Provide a predictable paginated response structure for list endpoints."""

    page_size_query_param = "page_size"
    max_page_size = 100