from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender")
    receiver = models.ManyToManyField(User, related_name="receiver")
    msg_body=models.CharField(max_length=1000)
    timestamp=models.DateTimeField(auto_now_add=True)
    unread=models.BooleanField(default = True)

