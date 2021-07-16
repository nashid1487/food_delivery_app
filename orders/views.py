from django.shortcuts import render, redirect, get_object_or_404
from food_delivery.models import Food
from .models import Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def _order_id(request):
    order = request.session.session_key
    if not order:
        request.session.create()
        order = request.session.create()
    return order


def add_order(request, food_id):
    food = Food.objects.get(id=food_id)
    try:
        order = Order.objects.get(order_id=_order_id(request))
    except Order.DoesNotExist:
        order = Order.objects.create(order_id=_order_id(request))
        order.save()
    try:
        order_item = OrderItem.objects.get(food=food, order=order)
        if order_item.food.available:
            order_item.quantity += 1
        order_item.save()
    except OrderItem.DoesNotExist:
        order_item = OrderItem.objects.create(food=food, quantity=1, order=order)
        order_item.save()
    return redirect('orders:order_detail')


def order_detail(request, total=0, count=0, order_items=None):
    try:
        order = Order.objects.get(order_id=_order_id(request))
        order_items = OrderItem.objects.filter(order=order, active=True)
        for order_item in order_items:
            total += (order_item.food.price*order_item.quantity)
            count += order_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'order.html', dict(order_items=order_items, total=total, count=count))


def remove_order(request, food_id):
    order = Order.objects.get(order_id=_order_id(request))
    food = get_object_or_404(Food, id=food_id)
    order_item = OrderItem.objects.get(food=food, order=order)
    if order_item.quantity > 1:
        order_item.quantity -= 1
        order_item.save()
    else:
        order_item.delete()
    return redirect('orders:order_detail')


def trash_item(request, food_id):
    order = Order.objects.get(order_id=_order_id(request))
    food = get_object_or_404(Food, id=food_id)
    order_item = OrderItem.objects.get(food=food, order=order)
    order_item.delete()
    return redirect('orders:order_detail')