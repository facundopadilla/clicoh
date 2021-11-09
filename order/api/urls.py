from django.urls import path

from .views import OrderViewSet

order_list = OrderViewSet.as_view({
    'get': 'list',
    'post': 'create'
    }
)

# Not to be confused with the application 'order_detail'. 
order_api_detail = OrderViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    }
)

order_get_total = OrderViewSet.as_view(
    {'get': 'get_total'}
)

name = 'order'
urlpatterns = [
    path('/order', order_list, name=name),
    path('/order/(?P&lt;pk&gt;[0-9]+)$', order_api_detail, name=name),
    path('/order/total/', order_get_total, name=name)
]