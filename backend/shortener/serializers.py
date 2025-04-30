from rest_framework import serializers
from django.conf import settings
from shortener.models import Link, Visit
from django.urls import reverse
from django.db.models import Max


class LinkSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and viewing ShortenedURL instances.
    """

    # Add a read-only field to display the full short URL
    short_url = serializers.SerializerMethodField(read_only=True)
    last_visit_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Link
        fields = [
            "url",
            "short_code",
            "short_url",  # custom field
            "created_at",
            "visit_count",
            "last_visit_at",
        ]
        read_only_fields = [
            "short_code",  # Generated internally, not provided by user
            "short_url",
            "created_at",
            "visit_count",
            "last_visit_at",
        ]

    def get_short_url(self, obj):
        """
        Constructs the full short URL using the request context.
        e.g., http://localhost:8000/abcdefg
        """
        request = self.context.get("request")
        if request is None or not obj.short_code:
            return None

        # Build the absolute base URL (e.g., http://localhost:8000) and append the short code.
        # Requires urlpattern named 'redirect-short-url'.
        try:
            path = reverse("redirect-short-url", kwargs={"short_code": obj.short_code})
            return request.build_absolute_uri(path)
        except Exception:
            # Fallback URL
            return f"{request.scheme}://{request.get_host()}/{obj.short_code}"

    def get_last_visit_at(self, obj):
        """Returns the timestamp of the most recent visit."""
        # This also performs a query per object.
        last_visit = obj.visits.aggregate(latest_visit=Max("timestamp"))
        return last_visit.get("latest_visit")


class VisitSerializer(serializers.ModelSerializer):
    """
    Serializer for Visit instances.
    """

    class Meta:
        model = Visit
        fields = [
            "timestamp",
            "ip_address",
            "user_agent",
        ]
        read_only_fields = fields  # All fields are read-only
