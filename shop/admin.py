from django.contrib import admin
from .models import Productos, Customer, Order, OrderItem, ShippingAddress

admin.site.register(Productos)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
