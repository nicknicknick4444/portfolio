from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from .forms import CustomUserCreationForm, CustomUserChangeForm
#from .models import CustomUser

# Register your models here.

# class CustomUserAdmin(UserAdmin):
#     #add_form = CustomUserCreationForm
#     #form = CustomUserChangeForm
#     #model = CustomUser
#     model = User
#     list_display = ["email",
#                     "username",
#                     "email",
#                     #"short_name",
#                     "is_staff"]
#     #fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("short_name",)}),)
#     fieldsets = UserAdmin.fieldsets
#     #add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("short_name",)}),)
#     add_fieldsets = UserAdmin.add_fieldsets
# 
# #admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(user, UserAdmin)
