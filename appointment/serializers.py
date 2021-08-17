from rest_framework import fields, serializers
from .models import *
from spplitAccount.serializers import UserSerializer

class AppointmentListSerializer(serializers.ModelSerializer):
    user1_name = serializers.ReadOnlyField(source='user1.username')
    user2_name = serializers.ReadOnlyField(source='user2.username')

    class Meta:
        model = AppointmentList
        fields = ('id', 'user1_name', 'user2_name', 'title', 'content', 'appointment_date', 'is_active',)

class AppointmentRequestSerializer(serializers.ModelSerializer):

    sender_name = serializers.ReadOnlyField(source='sender.username')
    receiver_name = serializers.ReadOnlyField(source='receiver.username')

    class Meta:
        model = AppointmentRequest
        fields = ('id', 'sender_name', 'receiver_name', 'title',  'content', 'register_date', 'appointment_date', "is_active", )