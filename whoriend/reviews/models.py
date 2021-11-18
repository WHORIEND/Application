from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    review = models.TextField(null = True,blank=True)
    time = models.IntegerField(null = True,validators=[MinValueValidator(1), MaxValueValidator(5)])
    good_teach = models.IntegerField(null = True,validators=[MinValueValidator(1), MaxValueValidator(5)])
    kind = models.IntegerField(null = True,validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=CASCADE)
    