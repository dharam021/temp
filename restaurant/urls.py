from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.RestaurantListView.as_view() ,name='list'),
    path('menu/<pk>',views.RestaurantDetailView.as_view() , name='menu'),      
]