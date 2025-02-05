from django.contrib import admin
from django.contrib.auth.models import User, Group
from ecommerce.models import Product, Customer,Attribute,AttributeValue,ProductAttribute,Image,Specification
from baton.models import BatonTheme
# Register your models here.

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(BatonTheme)
# admin.site.register(Image)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product','image')
    search_fields = ('product__name',)
admin.site.register(Specification)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price',]
    search_fields = ['name',]
    list_filter = ('name',)

    # def Imagecount(self,product):
    #     return product.image.count()


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email',]
    search_fields = ['email',]



admin.site.register(Attribute)
admin.site.register(AttributeValue)
# admin.site.register(ProductAttribute)
@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['product', 'attribute',]
    search_fields = ['product__name']
