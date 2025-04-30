from django.db import models


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
    visit_count = models.PositiveIntegerField(default=0)  # denormalized value

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        # Truncate original URL for display
        display_url = (self.url[:75] + "...") if len(self.url) > 75 else self.url
        return f"{self.short_code} -> {display_url}"
