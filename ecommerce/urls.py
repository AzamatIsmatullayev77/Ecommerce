from django.contrib import admin
from django.urls import path
from ecommerce import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('grid/', views.grid, name='grid'),
    path('detail/',views.product_detail, name='product_detail'),
    path('customers/',views.customers, name='customers'),
    path('customers-detail/',views.customers_detail, name='customers_detail'),
    # path('',views.index,name='index'),
]
