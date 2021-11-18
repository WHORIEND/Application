from django.db import models
from django.db.models.deletion import CASCADE
from main import models as main_models

# Create your models here.

class Category(main_models.TimeStampedModel):

    """category model definition"""
    name = models.CharField(max_length=30, null = True, unique=True)
    id = models.AutoField
    
    def __str__(self):
        return self.name

class Detail_Category(main_models.TimeStampedModel):
    category_name = models.ForeignKey(Category,db_column='name', on_delete=CASCADE)
    detail_name = models.CharField(max_length=30, default="")
    image = models.ImageField(null = True)

    def __str__(self):
        return self.detail_name