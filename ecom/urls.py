
from django.contrib import admin
from django.urls import path, include
from authentication import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("i18n/", include("django.conf.urls.i18n")),
    path('', include('shop.urls')),
    path('', include('api.urls')),
    path('login_user/', user_view.login_user, name='login_user'),
    path('logout_user/', auth.LogoutView.as_view(template_name='shop/body.html'),
         name='logout_user'),
    path('register/', user_view.register, name='register'),
    path('activate-user/<uidb64>/<token>',
         user_view.activate_user, name='activate'),
]
    
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

