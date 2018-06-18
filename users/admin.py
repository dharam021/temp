from django.contrib import admin
from .forms import UserCreationForm
from users.models import Customer, Owner , User
from django.contrib.auth.admin import UserAdmin

# class UserAdmin(BaseUserAdmin):
#     add_form = UserCreationForm
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username','email', 'first_name', 'last_name', 'is_customer' , 'is_owner', 'password1', 'password2')}
#         ),
#     )
admin.site.register(User,UserAdmin)
admin.site.register(Customer)
admin.site.register(Owner)
# admin.site.register(User)
# Register your models here.
