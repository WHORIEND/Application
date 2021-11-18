from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)
class ReviewAdmin(admin.ModelAdmin):
    
    list_display = (
        "name",
    )


@admin.register(models.Detail_category)
class Detail_categoryAdmin(admin.ModelAdmin):
    pass