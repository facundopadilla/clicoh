from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ..models import OrderDetail

from collections import OrderedDict

from typing import Union

class OrderDetailSerializer(ModelSerializer):
    total = SerializerMethodField()  # target: get_total
    total_usd = SerializerMethodField()  # target: get_total_usd
    _usd_blue_price = None

    def get_total(self, instance: Union[OrderDetail, OrderedDict]) -> float:
        if isinstance(instance, OrderedDict):
            total = instance['product'].price * instance['cuantity']
        else: 
            total = instance.product.price * int(instance.cuantity)
        return float(total)
    
    def get_total_usd(self, instance: Union[OrderDetail, OrderedDict]) -> float:
        from requests import get
        str2float = lambda value: float(value.replace(",", "."))
        if not self._usd_blue_price:
            data = get(url="https://www.dolarsi.com/api/api.php?type=valoresprincipales").json()
            usd_blue_price = str2float(data[1]['casa']['compra'])
            self._usd_blue_price = usd_blue_price
        if isinstance(instance, OrderedDict):
            price_usd = (instance['product'].price * instance['cuantity']) / self._usd_blue_price
        else:
            price_usd = (instance.product.price * int(instance.cuantity)) / self._usd_blue_price
        return round(price_usd, 2)

    class Meta:
        model = OrderDetail
        fields = ["id", "cuantity", "order", "product", "total", "total_usd"]
