from django.db.models.query import QuerySet
from django.http import response
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from core.models import User, SessionRegistrant, Session

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username'
        ]


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