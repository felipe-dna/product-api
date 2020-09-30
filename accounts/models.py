"""Contains the accounts app models."""
import uuid

from django.contrib.auth.models import AbstractUser
from djongo import models


class User(AbstractUser, models.Model):
    """Define the user model."""
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(max_length=300, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

    def get_full_name(self) -> str:
        """
        Return a combination between the first and last name of the user.

        :return: The combination between the first and last name of the user.
        :rtype: str
        """

        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        """
        Return the User instance string representation.
        """
        return f"{id} - {self.get_full_name()}"
