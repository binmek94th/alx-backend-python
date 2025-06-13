from django.db import models

class UnreadMessagesManager(models.Manager):
    def for_user(self, user):
        return (
            super()
            .get_queryset()
            .filter(receiver=user, read=False)
            .only('id', 'sender', 'content', 'created_at')
        )
