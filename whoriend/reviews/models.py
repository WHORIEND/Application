from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

star_range = zip(range(1, 5), range(1, 5))

class Review(AbstractUser):
    Time_Compliance = models.IntegerField(choices=star_range, blank=True) #1~5값만 가능
    Good_Teaching = models.IntegerField(choices=star_range, blank=True) #1~5값만 가능
    Nice_Value = models.IntegerField(choices=star_range, blank=True) #1~5값만 가능
    UID = models.ForeignKey("users", related_name = "users", on_delete=models.CASCADE, db_column="UID")
    