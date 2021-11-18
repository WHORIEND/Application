from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    review = models.TextField(blank=True)
    time = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    good_teach = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    kind = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=CASCADE)
    