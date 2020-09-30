"""Contains the product filter sets."""
import django_filters


class ProductFilterSet(django_filters.FilterSet):
    """Define the product filter set."""
    cost_lower_than = django_filters.NumberFilter(
        field_name="cost",
        lookup_expr="lt",
        label="cost-lower-than"
    )
    cost_great_than = django_filters.NumberFilter(
        field_name="cost",
        lookup_expr="gt",
        label="cost-great-than"
    )
    price_lower_than = django_filters.NumberFilter(
        field_name="price",
        lookup_expr="lt",
        label="price-lower-than"
    )
    price_great_than = django_filters.NumberFilter(
        field_name="price",
        lookup_expr="gt",
        label="price-great-than"
    )
    quantity_lower_than = django_filters.NumberFilter(
        field_name="quantity",
        lookup_expr="lt",
        label="quantity-lower-than"
    )
    quantity_great_than = django_filters.NumberFilter(
        field_name="quantity",
        lookup_expr="lt",
        label="quantity-great-than"
    )
