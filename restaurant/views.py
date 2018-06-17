from django.shortcuts import render,redirect
from django.views.generic import ListView , DetailView
from restaurant.models import Restaurant , FoodItem
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
	def get_context_data(self , *args , **kwargs):
		context = super(RestaurantDetailView , self).get_context_data(*args , **kwargs)
		# print(context)
		# print(context['object'].dishes.all())
		return context
	context_object_name = 'restaurant_obj'
