from django.urls import path,include
# import correct below
from ecommerce import views
urlpatterns = [
    path('',views.index , name='index'),
       
]