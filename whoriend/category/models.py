from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.name

class Detail_category(models.Model):
    category_name = models.ForeignKey(Category, on_delete=CASCADE)
    detail_name = models.CharField(max_length=30, default="")
    
    def __str__(self):
        return self.detail_name