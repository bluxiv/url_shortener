from rest_framework import generics, permissions, status, serializers, viewsets
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django.db import IntegrityError
from django.shortcuts import redirect, get_object_or_404
from django.http import Http404
from django.utils import timezone
from django.urls import reverse

from shortener.models import Link, Visit
from shortener.serializers import LinkSerializer, VisitSerializer
from shortener.utils import generate_short_code, get_client_ip, CustomPagination


# API Views
class LinkViewSet(viewsets.ModelViewSet):
    """
    API endpoints for creating, listing, and retrieving Shortened URLs.

    Provides:
    - `POST /api/links/`: Create a new link.
    - `GET  /api/links/`: List links (ordered by most visits by default).
    - `GET  /api/links/{short_code}/`: Retrieve a specific link.
    """

    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    lookup_field = "short_code"
    permission_classes = [permissions.AllowAny]

    filter_backends = [
        OrderingFilter,
    ]
    ordering_fields = ["visit_count", "created_at"]
    ordering = ["-visit_count"]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        """
        Generate a unique short_code before saving the instance.
        """
        MAX_ATTEMPTS = 10  # Prevent potential infinite loops
        attempts = 0
        while attempts < MAX_ATTEMPTS:
            code = generate_short_code()
            if not Link.objects.filter(short_code=code).exists():
                # Found a unique code
                try:
                    # Save the instance with the generated code
                    serializer.save(short_code=code)
                    return
                except IntegrityError:
                    # a race condition occurred.
                    pass  # Let the loop try again
                except Exception as e:
                    # Catch other potential save errors
                    raise serializers.ValidationError(
                        f"An unexpected error occurred during save: {e}"
                    ) from e

            attempts += 1

        # In the unlikely case of not generating a unique code
        raise serializers.ValidationError(
            "Could not generate a unique short code. Please try again."
        )

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


def redirect_view(request, short_code):
    """
    Redirects the user from the short URL to the original URL.
    Increments the click count.
    """
    url_obj = get_object_or_404(Link, short_code=short_code)

    # Log the visit
    Visit.objects.create(
        link=url_obj,
        ip_address=get_client_ip(request),
        user_agent=request.META.get("HTTP_USER_AGENT", None),
    )

    # Perform the redirect
    return redirect(url_obj.url)


class LinkVisitListView(generics.ListAPIView):
    """
    API endpoint to list recent visits for a specific Shortened URL.

    Provides:
    - `GET /api/links/{link_short_code}/visits/`: List visits for the link.
                                                Ordered by most recent first.
    """

    serializer_class = VisitSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = CustomPagination

    def get_queryset(self):
        """
        Filter visits based on the 'link_short_code' from the URL
        """
        link_short_code = self.kwargs.get("link_short_code")
        if not link_short_code:
            return Visit.objects.none()

        link = get_object_or_404(Link, short_code=link_short_code)

        return link.visits.all().order_by("-timestamp")  # type: ignore
