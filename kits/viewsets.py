"""Contains the kits app view sets."""
from typing import Any, List, Dict, Tuple
from rest_framework import serializers

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from kits.models import Kit, KitItem
from kits.serializers import KitsSerializer
from products.models import Product


class KitsViewSet(APIView):
    """Define the kits view set."""
    queryset = Kit.objects.all()
    serializer_class = KitsSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        """
        Create an new kit in the database.

        :param request: An http request.
        :type request: Request.

        :return: An http response.
        :rtype: Response.
        """
        validated_data = request.data

        self.__validate_kit_parameters_on_create(validated_data)

        # Saving the kit items.
        product_list = validated_data.get("products")
        kit_items_list = self.__create_kit_items(kit_items_list=product_list)

        kit_cost, kit_price, kit_stock = self.__calculate_cost_price_and_stock(kit_items_list=kit_items_list)

        # Saving the kit.
        new_kit = Kit(
            name=validated_data.get("name"),
            sku=validated_data.get("sku"),
            cost=kit_cost,
            price=kit_price,
            stock=kit_stock
        )

        new_kit.save()
        new_kit.products.set(kit_items_list)
        new_kit.save()

        serialized_kit_object = self.__serialize_kit(new_kit)

        return Response(serialized_kit_object, status=status.HTTP_201_CREATED)

    @staticmethod
    def __validate_kit_parameters_on_create(parameters: Dict[str, Any]) -> None:
        """
        Validate the given body parameters when creating a new kit.

        :param parameters: The given body parameters.
        :type parameters: Dict[str, Any]
        """
        valid_fields = ["name", "sku", "products"]

        # Validating the given parameters.
        for current_field_name in parameters.keys():
            if current_field_name not in valid_fields:
                raise serializers.ValidationError(f"{current_field_name} is not valid.")

        # Validating the required fields.
        for current_required_field in valid_fields:
            if current_required_field not in parameters.keys():
                raise serializers.ValidationError(f"Missing required parameter `{current_required_field}`.")

        # Validating the sku parameter.
        retrieved_kits = Kit.objects.filter(sku=parameters["sku"])

        if len(retrieved_kits) > 1:
            raise serializers.ValidationError(f"A kit with sku `{parameters['sku']}` already exists.")

    @staticmethod
    def __calculate_cost_price_and_stock(kit_items_list: List[KitItem]) -> Tuple[float, float, int]:
        """
        Calculate the final cost, price and available stock for the given kit.

        :param kit_items_list: A list of kit items.
        :type kit_items_list: List[KitItem].

        :return: A tuple containing the final cost, price and available stock.
        :rtype: Tuple[float, float int].
        """

        kit_cost = 0.0
        kit_price = 0.0
        max_quantity_of_kits = 0

        for current_kit_item in kit_items_list:
            kit_cost += (current_kit_item.product.cost * current_kit_item.quantity)

            current_products_price = current_kit_item.product.price * current_kit_item.quantity
            kit_price += (current_products_price - ((current_products_price * current_kit_item.discount) / 100))

            possible_kits_quantity_for_this_product = current_kit_item.product.quantity / current_kit_item.quantity

            if max_quantity_of_kits == 0:
                max_quantity_of_kits = possible_kits_quantity_for_this_product
            elif possible_kits_quantity_for_this_product < max_quantity_of_kits:
                max_quantity_of_kits = possible_kits_quantity_for_this_product

        return kit_cost, kit_price, max_quantity_of_kits

    @staticmethod
    def __create_kit_items(kit_items_list: List[Dict[str, Any]]) -> List[KitItem]:
        """
        Create a list of kit items in the database.

        :param kit_items_list: A list of kit items parameters to create them.
        :type kit_items_list: List[Dict[str, Any]].

        :return: A list with the created kit items.
        :rtype: List[KitItem]
        """

        valid_fields = ["sku", "quantity", "discount"]

        for current_kit_item_to_create in kit_items_list:
            for current_field_name in current_kit_item_to_create.keys():
                if current_field_name not in valid_fields:
                    raise serializers.ValidationError(f"{current_field_name} is not valid.")

        created_kit_items_list = []

        for current_product_to_create in kit_items_list:
            current_product_sku = current_product_to_create.get("sku")
            product = Product.objects.filter(sku=current_product_sku)

            if len(product) == 0:
                raise serializers.ValidationError(f"Product with sku `{current_product_sku}` does not exist.")

            new_kit_item = KitItem(
                product=product[0],
                quantity=current_product_to_create.get("quantity"),
                discount=current_product_to_create.get("discount"),
            )

            new_kit_item.save()
            created_kit_items_list.append(new_kit_item)

        return created_kit_items_list

    @staticmethod
    def __serialize_kit(kit_object: Kit) -> Dict[str, Any]:
        """
        Serialize a kit object.

        :param kit_object: The kit object instance that will be serialized.
        :type kit_object: Kit.

        :return: The serialized kit object in JSON format.
        :rtype: Dict[str, Any]
        """

        product_list = []
        for current_kit_item in kit_object.products.all():
            product_list.append({
                "sku": current_kit_item.product.sku,
                "quantity": current_kit_item.quantity,
                "discount": f"{current_kit_item.discount}%"
            })

        kit_dict = {
            "id": str(kit_object.id),
            "name": kit_object.name,
            "sku": kit_object.sku,
            "price": kit_object.price,
            "cost": kit_object.cost,
            "stock": kit_object.stock,
            "products": product_list
        }

        return kit_dict
