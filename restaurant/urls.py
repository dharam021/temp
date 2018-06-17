from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.RestaurantListView.as_view()),
    path('menu/<pk>',views.RestaurantDetailView.as_view() , name='menu'),      
]