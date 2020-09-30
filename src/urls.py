from django.urls import path, include

from accounts.routes import accounts_routes

urlpatterns = [
    path("users", include(accounts_routes.urls)),
    path("users/authenticate", include('rest_framework.urls', namespace='rest_framework'))
]
