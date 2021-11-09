from django.db import models

class Order(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    date_time = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.title}"