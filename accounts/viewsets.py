"""Contains the accounts app view sets."""
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Define the Users entity view set."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["POST"]




