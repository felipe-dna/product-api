from django.urls import path, include
from accounts.urls import urlpatterns

app_name = "accounts"

urlpatterns = [
    path("users/", include(urlpatterns)),
]
