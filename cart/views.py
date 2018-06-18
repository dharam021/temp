from django.shortcuts import render,redirect
from .models import Cart
from users.models import Customer , Owner
from django.http import Http404
from restaurant.models import Restaurant,FoodItem
from django.urls import reverse
def create(user , cart_id):
	pass

def index(request):
	rest = Restaurant.objects.first()
	print(request.session.get("cart_id" , None))
	print(request.user)
	cart_obj = Cart.objects.new_or_create(request,rest)

	return render(request,'cart/home.html',{})

# def update(request):
# 	cur_res = request.session.get('cur_res')
# 	restaurant = Restaurant.objects.filter(id = cur_res)
# 	cart_obj = Cart.objects.new_or_create(request,restaurant)
# 	item = FoodItem.objects.first()
# 	print(item)
# 	if item in cart_obj.items.all(): 
# 		cart_obj.items.remove(item)
# 	else:
# 		cart_obj.items.add(item)

# 	return render(request,'cart/home.html',{})

def update(request ,pk):
	rest_id = request.POST.get('rest_id')
	restaurant = Restaurant.objects.get(pk = rest_id)
	cart_obj = Cart.objects.new_or_create(request,restaurant)
	remove = request.POST.get('remove')
	# if remove == '0':
	item = FoodItem.objects.get(pk=pk)
	print(pk)
	if remove == '1': 
		cart_obj.items.remove(item)
		# pass
	else:
		cart_obj.items.add(item)
	# else:


	return redirect(reverse('restaurant:menu', kwargs={'pk':rest_id}))

