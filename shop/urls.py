from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('authentication.urls')),
    path('catalogo/', views.catalogo, name="catalogo"),
    path('cart/', views.cart, name="cart"),
    path('product/<str:pk>/', views.product, name="product"),
    path('update_item/', views.updateItem, name="updateItem"),
    path('checkout/', views.checkout, name="checkout"),
    path('process_order/', views.processOrder, name="processOrder"),
    # path('user/', views.userPage, name="user-page"),
    # path('account/', views.accountSettings, name="account"),

    # path('customer/<str:pk_test>/', views.customer, name="customer"),
    # path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    # path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    # path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]

handler404 = "helpers.views.handle_not_found"
handler500 = "helpers.views.handle_server_error"
