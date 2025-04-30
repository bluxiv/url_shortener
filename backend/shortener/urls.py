from django.urls import path
from shortener import views

urlpatterns = [
    # DRF endpoint for creating short URLs
    path("api/shorten/", views.LinkCreateView.as_view(), name="create_short_url"),
    # Django view for handling the actual redirection
    # The name 'redirect_short_url' is used by the serializer's get_short_url method
    path("<str:short_code>/", views.redirect_view, name="redirect_short_url"),
]
