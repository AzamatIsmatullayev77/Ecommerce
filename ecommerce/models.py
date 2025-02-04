from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    Specifications = models.TextField()
    Review = models.TextField()
    is_available = models.BooleanField()
    rating = models.FloatField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    description = models.TextField()
    vat_number = models.IntegerField()

    def __str__(self):
        return self.name
