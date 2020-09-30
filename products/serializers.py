"""Contains the products app serializers."""
from typing import Any, Dict

from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Define the serializer for the Product model."""

    class Meta:
        model = Product
        fields = ["id", "name", "sku", "cost", "price", "quantity"]
        extra_kwargs = {
            "id": {
                "read_only": True
            }
        }

    @staticmethod
    def validate_sku(sku: str) -> str:
        """"""

        retrieved_products = Product.objects.filter(sku=sku)

        if len(retrieved_products) >= 1:
            raise serializers.ValidationError(f"A product with sku `{sku}` already exists.")

        return sku

    def create(self, validated_data: Dict[str, Any]) -> Product:
        """"""
        new_product = Product(**validated_data)
        new_product.save()

        return new_product

    def update(self, instance: Product, validated_data: Dict[str, Any]) -> Product:
        """"""
        allowed_fields_to_update = ["name", "cost", "price", "quantity"]

        for current_field in allowed_fields_to_update:
            setattr(instance, current_field, validated_data.get(current_field, getattr(instance, current_field)))

        instance.save()

        return instance
