from itertools import product

from django.shortcuts import render,get_object_or_404
from django.template.context_processors import media

from ecommerce.models import Product, ProductAttribute, Customer,Image


# Create your views here.


def index(request):
    products = Product.objects.all()
    product_images = Image.objects.all()
    product_attributes = ProductAttribute.objects.filter()

    context = {
        'products': products,
        'product_images': product_images,
        # 'product_id':product,
    }
    return render(request,'ecommerce/product-list.html',context=context)

def grid(request):
    return render(request,'ecommerce/product-grid.html')

def product_detail(request, pk):
    products = Product.objects.all().filter(pk=pk)

    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
        'produuucts': products,
    }
    return render(request,'ecommerce/product-details.html',context)

def customers(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request,'ecommerce/customers.html',context=context)

def customers_detail(request):
    customers = get_object_or_404(Customer)
    context = {
        'customers': customers,
    }

    return render(request,'ecommerce/customer-details.html')
