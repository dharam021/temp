from django.urls import path,include
from django.contrib.auth import views as auth_views
# import correct below
from . import views
urlpatterns = [
    path('login/',auth_views.login , name='login'),
    path('register/customer',views.customer_register,  name='customer_register'),
    path('register/owner',views.owner_register, name='owner_register'),
    # path('login/', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
    path('logout/',auth_views.logout ,{'next_page':'restaurant:list'}, name='logout')
       
]