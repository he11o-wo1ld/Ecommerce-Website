from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    discountPrice = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Order(models.Model):
    items = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=70)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    total = models.CharField(max_length=200)

    def __str__(self):
        return self.name
