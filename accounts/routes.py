"""Contains the accounts app routes."""
from rest_framework import routers

from accounts.viewsets import UserViewSet

# Default router.
accounts_routes = routers.DefaultRouter()

# Registering the routes.
accounts_routes.register("", UserViewSet)
