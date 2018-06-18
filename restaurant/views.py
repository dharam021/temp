from django.shortcuts import render,redirect
from django.views.generic import ListView , DetailView
from restaurant.models import Restaurant , FoodItem
from cart.models import Cart
class RestaurantListView(ListView):
	template_name = 'restaurant/restaurant_list.html'
	model = Restaurant
	queryset = Restaurant.objects.all()
	# print(queryset)
	def get_context_data(self , *args , **kwargs):
		context = super(RestaurantListView , self).get_context_data(*args , **kwargs)
		# print(context)
		return context
	context_object_name = 'restaurant_obj'

class RestaurantDetailView(DetailView):
	model = Restaurant
	# 
	def get_context_data(self , *args , **kwargs):
		request = self.request
		# print(request.GET)
	
		context = super(RestaurantDetailView , self).get_context_data(*args , **kwargs)
		restaurant = context['object']
		print(restaurant)
		cart_obj = Cart.objects.new_or_create(request,restaurant)
		context['cart']=cart_obj
		return context
	context_object_name = 'restaurant_obj'
