"""Contains the kits app models."""
import uuid

from djongo import models

from products.models import Product


class Kit(models.Model):
    """Define the kits model."""
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, unique=True)
    cost = models.FloatField()
    price = models.FloatField()
    stock = models.IntegerField()
    products = models.ManyToManyField(to=Product)

    def __str__(self) -> str:
        """
        Return the Kit instance string representation.
        """
        return f"{id} - name - sku - price"
