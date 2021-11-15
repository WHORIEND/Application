from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.

class category(models.model):
    name = models.CharField(max_length=30, primary_key=True)

class detail_category(models.model):
    cid = models.CharField(max_length=30, primary_key=True)
    name = models.ForeignKey("category.name", on_delete=CASCADE)
    detail_name = models.CharField(max_length=30)