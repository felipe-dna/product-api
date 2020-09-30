"""Contains the products app models."""
import uuid

from djongo import models

from accounts.models import User


class Product(models.Model):
    """Define the products model."""
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, unique=True)
    cost = models.FloatField()
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self) -> str:
        """
        Return the Product instance string representation.
        """
        return f"{id} - name - sku - price"
