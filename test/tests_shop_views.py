from multiprocessing import context
from django.test import TestCase, Client
from django.urls import reverse
from shop.models import Productos, Categories, Order, OrderItem, ShippingAddress
import json


class ShopViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('catalogo')
        self.product = Productos.objects.create(
            title="test1",
            capacity="test 256GB",
            description="TESTING",
            digital=False,
            price="5000",
            category="buds",
            productphoto="shop/catalogo/test.jpg"
        )
        Productos.objects.create(
            title="test2",
            capacity="test 512GB",
            description="TESTING2",
            digital=False,
            price="10000",
            category="muebleria",
            productphoto="shop/catalogo/test.jpg"
        )

    def test_catalog_view_GET(self):
        self.client = Client()
        response = self.client.get(reverse('catalogo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/catalogo.html')
        self.product = Productos.objects.get(product=self.product)
        
    def test_catalog_categories_filter(self):
        self.client = Client()
        response = self.client.get(reverse('catalogo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/catalogo.html')
        self.product = Productos.objects.get(product=self.product)


    def cart_views_POST_product_to_cart(self):
        self.client = Client()
        response = self.client.post(
            reverse('cart'), {'productId': 1, 'action': 'add'})
        response = self.client.post(
            reverse('cart'), {'productId': 2, 'action': 'add'})
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'shop/cart.html')

    def cart_views_GET(self):
        self.client = Client()
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/cart.html')
        self.product = context.objects.get(
            items=self.items,
            order=self.order,
            cartItems=self.cartItems
        )

    def checkout(self):
        self.client = Client()
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/checkout.html')
        self.product = context.objects.post(
            items=self.items,
            order=self.order,
            cartItems=self.cartItems
        )
