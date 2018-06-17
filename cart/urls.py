from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('update/',views.update),
    # path('menu/<pk>',views.RestaurantDetailView.as_view() , name='menu'),      
]