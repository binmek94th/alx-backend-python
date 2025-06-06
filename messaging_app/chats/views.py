from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from chats.models import Conversation, Message
from chats.permissions import IsOwnerOrReadOnly, IsParticipant, IsConversationParticipant
from chats.serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filters = {
        'participants__username': ['exact', 'icontains'],
        'participants__email': ['exact', 'icontains'],
    }
    status = ''

    permission_classes = [IsAuthenticated, IsConversationParticipant]

    def get_queryset(self):
        conversation_id = self.kwargs.get('conversation_id')
        if conversation_id:
            conversation = Conversation.objects.filter(id=conversation_id).first()
            if conversation and self.request.user in conversation.participants.all():
                return Message.objects.filter(conversation=conversation)
            else:
                raise PermissionDenied("You are not a participant of this conversation.")
        return Message.objects.none()


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)