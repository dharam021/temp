from django.db import models
from users.models import Customer
from restaurant.models import FoodItem , Restaurant , Menu

from django.db.models.signals import m2m_changed , pre_save
# Create your models here.
class CartManager(models.Manager):
	def new(self,user=None):
		return self.model.objects.create(user=user)
	def new_or_create(self , request):
		cart_id = request.session.get("cart_id" , None)
		user = request.user
		cust_obj = None
		qs = self.get_queryset()
		if user.is_authenticated:
				cust_obj = user.customer
		if qs.filter(id = cart_id).exists():
			# already in DB
			cart_obj = qs.get(id = cart_id)
			if user.is_authenticated and cart_obj.user is None:
				cart_obj.user = cust_obj
				cart_obj.save()
		else:
			cart_obj = Cart.objects.new(user=cust_obj)
			request.session['cart_id']=cart_obj.id
		return cart_obj

class Cart(models.Model):
	restaurant  = models.ForeignKey(Restaurant, related_name='order' , on_delete = models.CASCADE)
	user 		= models.ForeignKey(Customer ,null = True, on_delete = models.CASCADE)
	items 		= models.ManyToManyField(FoodItem , null = True , blank = True)
	total 		= models.DecimalField(default = 0.0 , max_digits = 100 , decimal_places = 2)
	subtotal	= models.DecimalField(default = 0.0 , max_digits = 100 , decimal_places = 2)
	updated 	= models.DateTimeField(auto_now = True)
	timestamp 	= models.DateTimeField( auto_now_add = True)
	objects 	= CartManager()
	def __str__(self):
		return str(self.id)

def m2m_changed_cart_signal(sender,instance,action,*args,**kwargs):
	total = 0
	items = instance.items.all()
	print(action)
	print(instance.total)
	for item in items:
		total+=item.price
	print(total)
	instance.subtotal = total
	instance.save()

def pre_save_cart_signal(sender , instance , *args , **kwargs ):
	if instance.subtotal > 0:
		instance.total = instance.subtotal
	else:
		instance.total = 0.00

pre_save.connect(pre_save_cart_signal , sender = Cart)
m2m_changed.connect(m2m_changed_cart_signal,sender = Cart.items.through)