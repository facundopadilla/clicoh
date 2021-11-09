from django.db import models

class Product(models.Model):
    name: str = models.CharField(max_length=100, null=False, blank=False, unique=True)
    price: float = models.FloatField(default=0.0)
    stock: int = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Product: {self.name}>"