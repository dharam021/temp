from django.contrib import admin
from restaurant.models import Restaurant , FoodItem , Menu
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(FoodItem)
admin.site.register(Menu)