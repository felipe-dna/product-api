"""Contains the accounts app serializers."""
from typing import Dict, Any

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.Serializer):
    """Define the serializer for the User model."""

    id = serializers.UUIDField(required=False)
    first_name = serializers.CharField(max_length=80)
    last_name = serializers.CharField(max_length=80)
    email = serializers.EmailField(max_length=150)
    password = serializers.CharField(max_length=200)

    @staticmethod
    def validate_password(password_value: str) -> str:
        """
        Hash value passed by user.

        :param password_value: password of a user.
        :type password_value: str.

        :return: a hashed version of the password.
        :rtype: str.
        """

        if len(password_value) < 8:
            raise serializers.ValidationError("Your password must be at least 8 characters.")

        return make_password(password_value)

    @staticmethod
    def validate_email(email: str) -> str:
        """
        Validate the given email.

        :param email: The given email.
        :type email: str.

        :return: The given email value.
        :rtype: str
        """
        user_email = User.objects.filter(email=email)

        if len(user_email) >= 1:
            raise serializers.ValidationError("This email already exists.")

        return email

    def create(self, validated_data: Dict[str, Any]) -> None:
        """
        Create a User in the database.

        :param validated_data: The parameters to create the new user.
        :type validated_data: Dict[str, Any]
        """

        return User.objects.create(**validated_data)

    @property
    def data(self) -> Dict[str, Any]:
        """
        Overwrite the `data` method to remove the `password` from the response.

        :return: The `data` parameter without `password`.
        :rtype: Dict[str, Any]
        """
        current_data = super().data
        current_data.pop("password", None)

        return current_data
