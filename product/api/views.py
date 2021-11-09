from .serializers import ProductSerializer
from ..models import Product
from rest_framework.viewsets import ModelViewSet

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()
        serializer.original_stock[self.request.data['name']] = self.request.data['stock']

        
