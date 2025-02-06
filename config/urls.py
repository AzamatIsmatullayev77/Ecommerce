from baton.autodiscover import admin
from django.urls import path, include
from django.conf.urls.static import static
from config import settings
urlpatterns = [
       # path('baton/', include('baton.urls')),

       path('admin/', admin.site.urls),
       path('baton/', include('baton.urls')),

       path('',include('ecommerce.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
