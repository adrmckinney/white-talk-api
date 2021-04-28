from django.db.models.query import QuerySet
from django.http import response
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from core.models import SessionRegistrant, Session # User
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password' )

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             'id',
#             'username',
#             'first_name',
#             'last_name',
#             'email'
#         ]


class SessionRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = SessionRegistrant
        fields = [
            'pk',
            'first_name',
            'last_name',
            'pronouns',
            'email',
            'comment',
            'session',
        ]

class SessionSerializer(serializers.ModelSerializer):
    session_registrants = SessionRegisterSerializer(many=True, read_only=True)

    class Meta:
        model = Session
        fields = [
            'pk',
            'title',
            'start_date',
            'end_date',
            'description',
            'session_status',
            'session_registrants',
        ]