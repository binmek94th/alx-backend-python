from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    age = models.DateField()


class Conversation(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    user2 = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

