from django.urls import path, include

app_name = "accounts"

urlpatterns = [
    path("users", include("accounts.urls")),
    path("products", include("products.urls"))
]
