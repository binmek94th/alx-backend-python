from rest_framework import serializers

from messaging.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

