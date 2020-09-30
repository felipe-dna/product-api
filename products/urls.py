"""Contains the products app routes."""
from django.urls import path

from products.viewsets import ProductViewSet

app_name = "products"

urlpatterns = [
    path("", ProductViewSet.as_view({"get": "list", "post": "create"})),
    path("<uuid:pk>", ProductViewSet.as_view({"get": "detail", "patch": "update", "delete": "delete"}))]
