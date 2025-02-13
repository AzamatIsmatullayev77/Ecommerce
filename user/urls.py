from baton.autodiscover import admin
from django.urls import path, include
from django.conf.urls.static import static
from config import settings
from user import views

app_name = 'user'
urlpatterns = [
       path('simple-login/', views.simple_login, name='simple_login'),
       path('simple-logout/', views.simple_logout, name='simple_logout'),
       path('simple-register/',views.register,name='simple_register'),
       path('forgot-password/', views.forgot_password, name='forgot_password'),
]
