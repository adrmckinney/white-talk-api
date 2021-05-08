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
            'username',
            'first_name',
            'last_name',
            'email'
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
            'confirm',
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
            'start_time',
            'end_time',
            'description',
            'session_status',
            'number_of_registrants',
            'facilitator',
            'session_registrants',
        ]
