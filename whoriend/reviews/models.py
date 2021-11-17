from django.db import models

# Create your models here.

star_range = zip(range(1, 5), range(1, 5))

class Review(models.Model):
    Time_Compliance = models.IntegerField(choices=star_range, blank=True) #1~5값만 가능
    Good_Teaching = models.IntegerField(choices=star_range, blank=True) #1~5값만 가능
    Nice_Value = models.IntegerField(choices=star_range, blank=True) #1~5값만 가능
    UID = models.ForeignKey("users.MyUser", related_name = "users", on_delete=models.CASCADE)
    