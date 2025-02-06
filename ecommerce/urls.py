from django.contrib import admin
from django.urls import path
from ecommerce import views
from config import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('grid/', views.grid, name='grid'),
    path('detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('customers/',views.customers, name='customers'),
    path('customers-detail/<int:pk>/',views.customers_detail, name='customers_detail'),
    path('create-customer/',views.customer_create, name='create_customer'),
    path('create_product',views.product_create,name='create_product'),
    # path('',views.index,name='index'),
]

# if settings.DEBUG:
#     urlpatterns
