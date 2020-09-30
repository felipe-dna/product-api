"""Contains the accounts app serializers."""
from typing import Dict, Any

from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.Serializer):
    """Define the serializer for the User model."""
    first_name = serializers.CharField(max_length=80)
    last_name = serializers.CharField(max_length=80)
    email = serializers.EmailField(max_length=150)
    password = serializers.CharField(max_length=200)

    def create(self, validated_data: Dict[str, Any]) -> None:
        """
        Create a User in the database.

        :param validated_data: The parameters to create the new user.
        :type validated_data: Dict[str, Any]
        """
        # TODO: cryptograph the user password and email.
        new_user = User(**validated_data)

        return new_user.objects.create()

