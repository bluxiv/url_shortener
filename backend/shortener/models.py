from django.db import models
from django.db.models import F


class Link(models.Model):
    """
    Model mapping between an original long URL and a random short code
    """

    url = models.URLField()
    short_code = models.CharField(
        max_length=10,
        unique=True,
        db_index=True,  # for faster lookups by short_code
    )
    created_at = models.DateTimeField(auto_now_add=True)
    visit_count = models.PositiveIntegerField(
        default=0,
        help_text="Denormalized count of visits.",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        # Truncate original URL for display
        display_url = (self.url[:75] + "...") if len(self.url) > 75 else self.url
        code = self.short_code or "[Not Saved Yet]"
        return f"{code} -> {display_url}"


class Visit(models.Model):
    """
    Records an individual visit (click) to a Link.
    """

    link = models.ForeignKey(
        Link, on_delete=models.CASCADE, related_name="visits", db_index=True
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"Visit to {self.link.short_code} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

    def save(self, *args, **kwargs):
        # increment the Link's visit count
        if self.pk is None:
            Link.objects.filter(pk=self.link.pk).update(
                visit_count=F("visit_count") + 1
            )

        return super().save(*args, **kwargs)
