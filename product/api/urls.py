from django.urls import path
from .views import ProductViewSet

product_list = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create'
    }
)

product_detail = ProductViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    }
)


name = 'products'
urlpatterns = [
    path('', product_list, name=name),
    path('/product/(?P&lt;pk&gt;[0-9]+)$', product_detail, name=name)
]