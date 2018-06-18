from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Customer , Owner , User


class CustomerForm(UserCreationForm):
	contact = forms.IntegerField(label = 'contact no ')
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('first_name' , 'last_name', 'username' , 'email')

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_customer = True
		# if commit
		user.save()
		customer = Customer(user=user)
		customer.save()
		
		return user





