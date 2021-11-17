from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, null=False, primary_key=True)

class Detail_category(models.Model):
    cid = models.CharField(max_length=30, null=False, primary_key=True)
    name = models.ForeignKey("category.Category", on_delete=CASCADE)
    detail_name = models.CharField(max_length=30)