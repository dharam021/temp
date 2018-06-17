from django.db import models
# from django.contrib.auth import User
from django.core.validators import URLValidator
from users.models import Owner

class RestaurantManager(models.Manager):
	def search(self , query):
		qs = self.get_queryset()
		return qs.filter(name__icontains=query)

class Restaurant(models.Model):
	name = models.CharField(max_length = 200)
	slug = models.SlugField(max_length = 15)
	email = models.EmailField(max_length = 254)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	website = models.TextField(validators=[URLValidator()])
	telephone = models.PositiveIntegerField()
	owner = models.ForeignKey(Owner , on_delete = models.CASCADE)
	image = models.ImageField(upload_to='restaurant/' , null = True , blank = True)
	objects = RestaurantManager()
	def __str__(self):
		return self.name

class FoodItem(models.Model):
	name = models.CharField(max_length = 200)
	price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to='dishes/' , null = True , blank = True)
	def __str__(self):
		return self.name;

class Menu(models.Model):
	title = models.CharField(max_length = 200)
	description = models.TextField(blank=True, null=True)
	restaurant = models.ForeignKey(Restaurant, null=True, related_name='menu' , on_delete = models.CASCADE)
	dishes = models.ManyToManyField(FoodItem, null=True, related_name='dishes' )

	def __str__(self):
		return self.title;
