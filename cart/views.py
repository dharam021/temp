from django.shortcuts import render
from .models import Cart
from users.models import Customer , Owner
from django.http import Http404
from restaurant.models import FoodItem
def create(user , cart_id):
	pass

def index(request):
	print(request.session.get("cart_id" , None))
	print(request.user)
	cart_obj = Cart.objects.new_or_create(request)

	return render(request,'cart/home.html',{})

def update(request):
	cart_obj = Cart.objects.new_or_create(request)
	item = FoodItem.objects.first()
	print(item)
	if item in cart_obj.items.all(): 
		cart_obj.items.remove(item)
	else:
		cart_obj.items.add(item)

	return render(request,'cart/home.html',{})

