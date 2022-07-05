from django.urls import path, include
from . import views
from authentication import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [
    path('', views.index, name='index'),
    path('login_user/', user_view.login_user, name='login_user'),
    path('logout_user/', auth.LogoutView.as_view(template_name='shop/body.html'),
         name='logout_user'),
    path('register/', user_view.register, name='register'),
    path('activate-user/<uidb64>/<token>',
         user_view.activate_user, name='activate'),
]
