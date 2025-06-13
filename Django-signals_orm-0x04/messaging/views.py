from messaging.models import Message
from django.contrib.auth import get_user_model

def create_message():
    User = get_user_model()

    user = User.objects.first()
    Message.objects.create(receiver=user, sender=user, content='dslkjflasdjflsadjlfsaj')


create_message()