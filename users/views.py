from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import CustomerForm
from .models import Customer , Owner

# Create your views here.
def customer_register(request):

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if user.is_authenticated and user.is_customer:
            	print("Customer")
            else:
            	print("Owner")
            return redirect('restaurant:list')
    else:
	    form = CustomerForm()
	    print(form)
    return render(request, 'registration/register1.html', {'form': form})

def owner_register(request):
	return render(request, 'registration/register1.html', {'form': form})