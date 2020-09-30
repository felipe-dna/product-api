"""Contains the products app view sets."""
from typing import Any
from uuid import UUID

from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from .filtersets import ProductFilterSet
from .models import Product
from .serializers import ProductCreateReadSerializer, ProductDeleteUpdateDetailSerializer


class ProductCreateRetrieveViewSet(viewsets.ModelViewSet):
    """Define the Product entity view set."""
    queryset = Product.objects.all()
    serializer_class = ProductCreateReadSerializer
    filterset_class = ProductFilterSet
    permission_classes = [IsAuthenticated]

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """"""

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Overwrite the create method to accept many items in the request.

        :param request: The http request.
        :type request: Request.

        :return: The response object.
        :rtype: Response.
        """
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProductUpdateDeleteDetailViewSet(viewsets.ModelViewSet):
    """Define the view set for delete, update and retrieve products."""
    queryset = Product.objects.all()
    serializer_class = ProductDeleteUpdateDetailSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request: Request, product_id: UUID) -> Response:
        """
        Overwrite the `retrieve` product method.

        :param request: The current http request.
        :type request: Request.

        :param product_id: The id of the product that will searched.
        :type product_id: UUID.

        :return: A http response.
        :rtype: Response.
        """
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=product_id)
        serializer = ProductDeleteUpdateDetailSerializer(product)

        return Response(serializer.data)
