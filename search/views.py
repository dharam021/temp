from django.shortcuts import render,redirect
from django.views.generic import ListView , DetailView
from restaurant.models import Restaurant

class SearchRestaurantView(ListView):
	template_name = 'search/search_restaurant.html'
	model = Restaurant
	def get_queryset(self , *args , **kwargs):
		request = self.request
		print(request)
		search_query = request.GET.get('q')
		if search_query is not None:
			return Restaurant.objects.search(search_query)
		return Restaurant.objects.all()
	
	def get_context_data(self , *args , **kwargs):
		context = super(SearchRestaurantView , self).get_context_data(*args , **kwargs)
		# print(context)
		return context

	context_object_name = 'restaurant_obj'
