"""Contains the accounts app routes."""
from rest_framework import routers

from accounts.viewsets import UserViewSet

# Default router.
accounts_routers = routers.DefaultRouter()

# Registering the routes.
accounts_routers.register("users", UserViewSet)
