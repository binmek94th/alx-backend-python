from rest_framework.permissions import BasePermission

from chats.models import Conversation


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsParticipant(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()


class IsAuthenticatedUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsConversationParticipant(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'GET', 'PUT', 'PATCH', 'DELETE']:
            conversation_id = view.kwargs.get('conversation_id')
            if conversation_id:
                try:
                    conversation = Conversation.objects.get(id=conversation_id)
                    return request.user in conversation.participants.all()
                except Conversation.DoesNotExist:
                    return False
        return False

