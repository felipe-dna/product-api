"""Contains the kits app serializers."""
from typing import Any, Dict, List

from rest_framework import serializers

from kits.models import KitItem, Kit
from products.models import Product


class KitsSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = Kit
        fields = "__all__"
        read_only_fields = ["id", "cost", "price", "stock"]
