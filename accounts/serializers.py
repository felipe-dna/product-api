"""Contains the accounts app serializers."""
from typing import Dict, Any

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from accounts.models import User


class UserSerializer(serializers.Serializer):
    """Define the serializer for the User model."""
    first_name = serializers.CharField(max_length=80)
    last_name = serializers.CharField(max_length=80)
    email = serializers.EmailField(max_length=150)
    password = serializers.CharField(max_length=200)
    api_key = serializers.CharField(max_length=300, allow_blank=True, required=False)

    def create(self, validated_data: Dict[str, Any]) -> None:
        """
        Create a User in the database.

        :param validated_data: The parameters to create the new user.
        :type validated_data: Dict[str, Any]
        """

        created_user = User(**validated_data)
        created_user.save()

        created_user_token = Token(user=created_user)
        created_user_token.save()

        self.password = None
        self.api_key = created_user_token.key
