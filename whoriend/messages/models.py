from django.db import models

# Create your models here.

class Message(models.model):
    sender_uid = models.ForeignKey("users", related_name="users", on_delete=models.CASCADE, db_column="UID") #보내는 사람 uid
    receiver_uid = models.ForeignKey("users", related_name="users", on_delete=models.CASCADE, db_column="UID") #받는 사람 uid
    content = models.TextField(max_length=500) #쪽지 내용 저장
    time = models.DateTimeField(auto_now = True) #레코드 갱신시 시간 자동저장