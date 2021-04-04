from rest_framework import serializers
from core.models import User, SessionRegister, Session

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username'
        ]

class SessionRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionRegister
        fields = [
            'pk',
            'name',
            'pronouns',
            'email',
            'comment'
        ]

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = [
            'pk',
            'title',
            'start_date',
            'end_date',
            'description'
        ]