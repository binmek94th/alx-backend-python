from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from chats.models import Conversation, Message
from chats.permissions import IsOwnerOrReadOnly, IsParticipant
from chats.serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filters = {
        'participants__username': ['exact', 'icontains'],
        'participants__email': ['exact', 'icontains'],
    }
    status = ''

    permission_classes = [IsAuthenticated, IsParticipant]



class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)