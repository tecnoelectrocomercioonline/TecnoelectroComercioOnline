from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import datetime
from django.contrib import messages
from .models import *
from .utils import cartData, guestOrder

def index(request):
	return render(request, 'shop/body.html', {'title': 'index'})

def HomeForm(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
    if form.is_valid():
            form.save()
            messages.success(request, 'Mensaje enviado con exito')
            return redirect('index')
    else:
        form = HomeForm()
    return render(request, 'shop/body.html', {'form': form})

def catalogo(request):
    data = cartData(request)
    cartItems = data['cartItems']
    # order = data['order']
    # items = data['items']
    products = Productos.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'shop/catalogo.html', context)

def product(request, pk):
	product = Productos.objects.get(id=pk)

	if request.method == 'POST':
		product = Productos.objects.get(id=pk)
		#Get user account information
		try:
			customer = request.user.customer	
		except:
			device = request.COOKIES['device']
			customer, created = Customer.objects.get_or_create(device=device)

		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
		orderItem.quantity=request.POST['quantity']
		orderItem.save()

		return redirect('cart')

	context = {'product':product}
	return render(request, 'shop/product.html', context)

def cart(request):
	try:
		customer = request.user.customer
		# customer = request.user.is_authenticated
	except:
		device = request.COOKIES['device']
		customer, created = Customer.objects.get_or_create(device=device)

	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	context = {'order':order}
	return render(request, 'shop/cart.html', context)

def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'shop/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Productos.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)
