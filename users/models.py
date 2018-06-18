from django.db import models
from django.contrib.auth.models import AbstractUser
 
class User(AbstractUser):
	is_owner = models.BooleanField(default=False)
	is_customer = models.BooleanField(default=False)
	
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE ,related_name = 'customer' , primary_key = 'True')
    contact = models.PositiveIntegerField()
    def __str__(self):
    	return self.user.username
 
class Owner(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE ,related_name = 'owner')
	# restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE ,related_name = 'owner')
	def __str__(self):
		return self.user.username