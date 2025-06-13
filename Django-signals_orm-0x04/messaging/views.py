from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from messaging.models import Message
from messaging.serializers import MessageSerializer


class delete_user(APIView):
    def delete(self, request):
        user = request.user
        if not user:
            return Response({"error": "User not found."}, status=404)
        if not user.is_authenticated:
            return Response({"error": "User not authenticated."}, status=401)
        user.delete()
        return Response({"message": "User account deleted successfully."}, status=204)


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return (Message.objects.filter(sender=user) | Message.objects.filter(receiver=user)).distinct()
        return Message.objects.none()