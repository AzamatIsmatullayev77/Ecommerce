from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['my_order']
        verbose_name = 'category'
        verbose_name_plural = "categories"


class Product(BaseModel):
    class RatingChoice(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    name = models.CharField(max_length=100)
    comment=models.TextField(blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    description = models.TextField()
    is_available = models.BooleanField()
    discount = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0,null=True,blank=True)
    class Meta:
        ordering = ['my_order']
        verbose_name = 'product'
        verbose_name_plural = "products"

    def __str__(self):
        return self.name


class Customer(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    Phone_number = PhoneNumberField(region="UZ",null=True,blank=True)
    Address = models.TextField(null=True,blank=True)
    description = models.TextField()
    vat_number = models.IntegerField()
    class Meta:
        ordering = ['my_order']
        verbose_name = 'customer'
        verbose_name_plural = "customers"

    def __str__(self):
        return self.name


class Image(BaseModel):
    image = models.ImageField(upload_to='media/media/', blank=True,null=True)
    class Meta:
        ordering = ['my_order']
    @property
    def get_absolute_url(self):
        return self.image.url
class ProductImage(BaseModel):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='images')

class Specification(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name



class Attribute(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AttributeValue(BaseModel):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value


class ProductAttribute(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,related_name='product_attributes', null=True, blank=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.SET_NULL, null=True, blank=True)
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.SET_NULL, null=True, blank=True)

