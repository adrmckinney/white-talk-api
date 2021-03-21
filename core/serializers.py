from rest_framework import serializers
from core.models import User, SessionRegister

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username'
        ]