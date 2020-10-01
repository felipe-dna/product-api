"""Contains the kits app routes."""
from django.urls import path

from kits.viewsets import KitsViewSet

app_name = "kits"

urlpatterns = [
    path("", KitsViewSet.as_view()),
]
