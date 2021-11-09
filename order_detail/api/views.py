from .serializers import OrderDetailSerializer
from ..models import OrderDetail
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from product.models import Product

import json

class OrderDetailViewSet(ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    original_stock = {}

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = request.data.get('product', None)
        cuantity = int(request.data.get('cuantity', None))
        product_instance = get_object_or_404(Product, pk=product)
        if product_instance.stock > cuantity:
            self._save_original_stock(product_instance.stock)
            product_instance.stock -= cuantity
            product_instance.save()
        else:
            return Response(data={"detail": "The amount of income exceeds the amount available"}, status=422)
        self.perform_create(serializer)
        return Response(serializer.data, status=200)
    
    def _save_original_stock(self, stock: int):
        self.original_stock[self.request.data["product"]] = stock

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(self.original_stock)
        # Is not persistent
        if self.original_stock:
            instance.product.stock = self.original_stock[str(instance.product.id)]
            instance.product.save()
        instance.delete()
        return Response(data={"detail": "Deleted success"}, status=204)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        product_instance = instance.product
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cuantity = int(request.data.get('cuantity', 0))
        if not cuantity:
            return Response(data={"detail": "The 'cuantity' field is not found or is not greater than zero."}, status=422)
        if product_instance.stock > cuantity:
            self._save_original_stock(product_instance.stock)
            product_instance.stock -= cuantity
            product_instance.save()
        else:
            return Response(data={"detail": "The amount of income exceeds the amount available"}, status=422)

        instance.cuantity = cuantity
        instance.save()
        return Response(serializer.data, status=200)