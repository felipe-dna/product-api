"""Contains the products app routes."""
from django.urls import path

from products.viewsets import ProductViewSet

app_name = "products"

urlpatterns = [
    path("", ProductViewSet.as_view())
]
