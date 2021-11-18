from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User

# Register your models here.
# @admin.register(models.User)




    
admin.site.register(User)