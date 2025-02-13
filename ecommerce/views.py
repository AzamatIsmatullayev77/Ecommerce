from itertools import product
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import media
from django.views.decorators.csrf import csrf_protect
from ecommerce.forms import CustomerModelForm, ProductModelForm
from ecommerce.models import Product, ProductAttribute, Customer,Image


# Create your views here.


def index(request):
    search_query = request.GET.get('q','')
    products = Product.objects.all()
    product_images = Image.image
    product_attributes = ProductAttribute.objects.filter()
    if search_query:
        products = products.filter(name__icontains=search_query)

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
    search_query = request.GET.get('q','')
    filter_type = request.GET.get('filter','')

    if filter_type=='filter':
        customers = Customer.objects.all().order_by('name')
    else:
        customers = Customer.objects.all().order_by('-id')

    if search_query:
        customers = customers.filter(name__icontains=search_query)
    context = {
        'customers': customers
    }
    return render(request,'ecommerce/customers.html',context=context)

def customers_detail(request,pk ):
    customers = get_object_or_404(Customer,pk=pk)
    cUstomers = Customer.objects.all().filter(pk=pk)
    context = {
        'customers': customers,
        'cUstomers': cUstomers,
    }

    return render(request,'ecommerce/customer-details.html',context=context)

def customer_create(request):
    form = CustomerModelForm()
    if request.method == 'POST':
        form = CustomerModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerModelForm()
    context = {
        'form': form,
    }
    return render(request,'ecommerce/creat.html',context=context)

def product_create(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductModelForm()
    context = {
        'form': form,
    }
    return render(request,'ecommerce/create_product.html',context=context)


