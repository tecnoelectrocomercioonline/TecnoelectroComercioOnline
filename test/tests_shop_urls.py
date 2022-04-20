from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shop.views import catalogo, cart, checkout, updateItem, processOrder

class Test(SimpleTestCase):

    def catalogo_url_is_resolved(self):
        url = reverse('catalogo')
        self.assertEquals(resolve(url).func, catalogo)

    def cart_url_is_resolved(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func, cart)

    def checkout_url_is_resolved(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func.view_class, checkout)

    def updateItem_url_is_resolved(self):
        url = reverse('update_item')
        self.assertEquals(resolve(url).func, updateItem)

    def processOrder_url_is_resolved(self):
        url = reverse('process_order')
        self.assertEquals(resolve(url).func, processOrder)
