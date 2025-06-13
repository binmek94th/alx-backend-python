from django.dispatch import receiver
from .models import Message, Notification, MessageHistory
from django.db.models.signals import post_save, pre_save

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(message=instance, user=instance.receiver)


@receiver(pre_save, sender=Message)
def create_message_history(sender, instance, **kwargs):
    if instance.pk and Message.objects.get(pk=instance.pk):
        MessageHistory.objects.create(message=instance)