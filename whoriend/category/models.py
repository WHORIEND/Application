from django.db import models
from django.db.models.deletion import CASCADE
from dja
# Create your models here.

class Category(models.model):
    Variety = models.CharField(primary_key=True, max_length=10)

class DetailCategory(models.model):
    Variety = models.ForeignKey("Category", on_delete=CASCADE)
    Cid = models.AutoField(primary_key=True)
    DetailVariety = models.CharField(max_length=10)