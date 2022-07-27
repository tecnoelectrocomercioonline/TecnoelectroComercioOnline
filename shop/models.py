from unicodedata import decimal
from django.db import models
from django.contrib.auth.models import User
# from authentication.models import Customer

class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    device = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=25, null=True)
    phone = models.CharField(max_length=25, null=True)
    address = models.TextField("Direccion", max_length=600, default='', blank=True)

    def __str__(self):
        if self.name:
            name = self.name
        else:
            name = self.device
        return str(name)

class Categories(models.TextChoices):
    SMARTPHONES = "smartphones"
    BUDS = "buds"
    WATCH = "watch"
    TABLETS = "tablets"
    LAPTOPS = "laptops"
    PANTALLAS = "pantallas"
    CONSOLAS = "consolas"
    MOTINOTRES = "monitores"
    CASE = "case"
    PROCESADOR = "procesador"
    MOTHERBOARD = "motherboard"
    SSD = "ssd"
    HDD = "hdd"
    RAM = "ram"
    COOLING = "cooling"
    FUENTE = "fuente"
    Mousse = "mousse"
    SILLAS = "sillas"
    TECLADO = "teclados"
    LENTES = "lentes"   
    HEADSET = "headsets"
    MANDOS = "mandos"   
    ELECTRODOMESTICOS = "lavadoras"
    MUEBLERIA = "refrigeradoras"
    COCINAS = "cocinas"
    CAMAS = "camas"
    TALADROS = "taladros"
    ESMALTES = "esmaltes"
    MAQUILLAJE = "maquillaje"
    BICICLETAS = "bicicletas"
    COLCHON = "colchon"


class Productos(models.Model):
    # user = models.ForeignKey(
    #     Customer, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=75)
    capacity = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    # price = MoneyField(max_digits=14, decimal_places=2, default_currency='CRC')
    # price = models.FloatField()
    category = models.CharField(max_length=20, choices=Categories.choices)
    productphoto = models.ImageField(
        null=True, blank=True, upload_to="shop/catalogo")
    # discount_price = models.FloatField()

    def __str__(self):
        return "{} : {} []".format(self.title, self.capacity, self.description, self.price, self.category, self.productphoto)

    @property
    def imageURL(self):
        try:
            url = self.productphoto.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
	product = models.ForeignKey(Productos, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
