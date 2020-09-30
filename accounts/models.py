"""Contains the accounts app models."""
import uuid

from djongo import models


class User(models.Model):
    """Define the user model."""
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=200)

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
