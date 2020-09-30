"""Contains the products app routes."""
from django.urls import path

from products.viewsets import ProductCreateRetrieveViewSet, ProductUpdateDeleteDetailViewSet

app_name = "products"

urlpatterns = [
    path("", ProductCreateRetrieveViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "/<uuid:product_id>",
        ProductUpdateDeleteDetailViewSet.as_view({
            "get": "retrieve",
            "patch": "update",
            "delete": "destroy"
        })
    )
]
