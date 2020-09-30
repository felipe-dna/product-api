"""Contains the accounts app routes."""
from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.viewsets import UserViewSet

app_name = "accounts"

urlpatterns = [
    path("", UserViewSet),
    path("authenticate", TokenObtainPairView.as_view()),
    path("refresh-token", TokenRefreshView.as_view()),
]

