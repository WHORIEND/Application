from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Fllowing)
class ReviewAdmin(admin.ModelAdmin):
    
    pass