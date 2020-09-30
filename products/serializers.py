"""Contains the products app serializers."""
from typing import Any, Dict

from rest_framework import serializers

from products.models import Product


class ProductCreateReadSerializer(serializers.ModelSerializer):
    """Define the serializer for the Product model."""

    class Meta:
        """Define the serializer metadata."""
        model = Product
        fields = ["id", "name", "sku", "cost", "price", "quantity"]
        extra_kwargs = {
            "id": {
                "read_only": True
            }
        }

    @staticmethod
    def validate_sku(sku: str) -> str:
        """
        Validate the sku field value.

        :param sku: The current sku.
        :type sku: str.

        :return: The sku value.
        :rtype: str.
        """

        retrieved_products = Product.objects.filter(sku=sku)

        if len(retrieved_products) >= 1:
            raise serializers.ValidationError(f"A product with sku `{sku}` already exists.")

        return sku

    def create(self, validated_data: Dict[str, Any]) -> Product:
        """
        Create a new product in the database.

        :param validated_data: The body parameters to create a new product.
        :type validated_data: Dict[str, Any].

        :return: The created product.
        :rtype: Product.
        """
        new_product = Product(**validated_data)
        new_product.save()

        return new_product


class ProductDeleteUpdateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        """Define the serializer metadata."""
        model = Product
        fields = ["id", "name", "sku", "cost", "price", "quantity"]
        extra_kwargs = {
            "id": {
                "read_only": True
            },
            "name": {
                "required": False
            },
            "sku": {
                "required": False
            },
            "cost": {
                "required": False
            },
            "price": {
                "required": False
            },
            "quantity": {
                "required": False
            },
        }

    def update(self, instance: Product, validated_data: Dict[str, Any]) -> Product:
        """
        Update an product in the database.

        :param instance: The current product instance.
        :type instance: Product.

        :param validated_data: The body parameters to update the product.
        :type validated_data: Dict[str, Any]

        :return: The product instance with the new data.
        :rtype: Product
        """
        allowed_fields_to_update = ["name", "cost", "price", "quantity"]

        for current_field in allowed_fields_to_update:
            if current_field not in allowed_fields_to_update:
                raise serializers.ValidationError(f"`{current_field}` is not a valid field.")

            setattr(instance, current_field, validated_data.get(current_field, getattr(instance, current_field)))

        instance.save()

        return instance
