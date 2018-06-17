from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.SearchRestaurantView.as_view(),name='query'),
]