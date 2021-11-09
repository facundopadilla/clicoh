from django.urls import path

from .views import OrderDetailViewSet

order_detail_list = OrderDetailViewSet.as_view({
    'get': 'list',
    'post': 'create'
    }
)

order_detail_detail = OrderDetailViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    }
)

name = 'orderdetail'
urlpatterns = [
    path('/order_detail', order_detail_list, name=name),
    path('/order_detail/(?P&lt;pk&gt;[0-9]+)$', order_detail_detail, name=name)
]