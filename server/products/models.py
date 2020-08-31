from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=200)
    api_id = models.CharField(max_length=30, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.URLField()
    last_check = models.DateTimeField(auto_now=True)
    ali_url = models.URLField()

    def __str__(self):
        return str(self.name)