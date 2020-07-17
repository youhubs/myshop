import datetime, json
from django.shortcuts import render
from django.http import JsonResponse

from .models import *
from . utils import cartData, cookieCart, guestOrder


# Create your views here.
def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
    
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/index.html', context)


def cart(request):
    data = cartData(request)
    order = data['order']
    items = data['items']
    cartItems = data['cartItems']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)
    order = data['order']
    items = data['items']
    cartItems = data['cartItems']
    
    context = {'items':items, 'order': order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)
    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()
    
    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)
    
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment complete!', safe=False)