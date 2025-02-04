from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'ecommerce/product-list.html')

def grid(request):
    return render(request,'ecommerce/product-grid.html')

def product_detail(request):
    return render(request,'ecommerce/product-details.html')


def customers(request):
    return render(request,'ecommerce/customers.html')

def customers_detail(request):
    return render(request,'ecommerce/customer-details.html')