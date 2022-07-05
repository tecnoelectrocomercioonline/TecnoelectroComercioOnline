
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("i18n/", include("django.conf.urls.i18n")),
    path('', include('shop.urls')),
    path('', include('authentication.urls')),
    path('', include('api.urls')),
]
    
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

