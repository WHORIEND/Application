from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class message(models.model):
    Sender_uid = models.ForeignKey("user.User", on_delete=CASCADE)
    Receiver_uid = models.ForeignKey("user.User", on_delete=CASCADE)
    Content = models.CharField(max_length=500)
    Time = models.DateTimeField(auto_now_add=True)