from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE

# Create your models here.

class Review(models.model):
    TimePromise = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    Degree_teaching = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    Nice = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    UID = models.ForeignKey("user.User", on_delete=CASCADE)
