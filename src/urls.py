from django.urls import path, include

urlpatterns = [
    path("users", include("accounts.urls")),
    path("products", include("products.urls")),
    path("kits", include("kits.urls"))
]
