from rest_framework import serializers

from .models import User, Conversation, Message


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'age']
        read_only_fields = ['user_id']


class ConversationSerializer(serializers.Serializer):
    participants = UsersSerializer(many=True, read_only=True)
    messages = serializers.SerializerMethodField()

    class Meta:
        model: Conversation
        fields = '__all__'
        read_only_fields = ['conversation_id']

    def get_messages(self, obj):
        messages = obj.message_set.all()
        return MessageSerializer(messages, many=True).data


class MessageSerializer(serializers.Serializer):

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['message_id', 'sent_at', 'created_at']