from django.test import TestCase
from shop.models import Productos, Order, OrderItem, ShippingAddress


class Customer(TestCase):
    def setUp(self):
        Productos.objects.create(
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

    def test_products(self):
        test1 = Productos.objects.get(title="test1")
        test2 = Productos.objects.get(title="test2")
        self.assertEqual(test1)
        self.assertEqual(test2)
