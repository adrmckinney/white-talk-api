from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FormParser, JSONParser
from core import serializers
from core.models import User, SessionRegister
from core.serializers import UserSerializer, SessionRegisterSerializer
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        # takes all the user info and turns it into JSON
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class SessionRegisterView(ListCreateAPIView):
    queryset = SessionRegister.objects.all()
    serializer_class = SessionRegisterSerializer
    permission_classes = [permissions.AllowAny]
    def perform_create(self, serializer):
        # breakpoint()
        template = render_to_string('base/email_template.html', 
                                    {
                                        'name': serializer.validated_data["name"]
                                    })
        email = EmailMessage(
            'test email from Django',
            template,
            settings.EMAIL_HOST_USER,
            ['adrmckinney@icloud.com'],
            # [serializer.validated_data["email"]]
        )
        email.fail_silently = False
        email.send()
        
        serializer.save()
        
    def get(self, request):
        session_registrations = SessionRegister.objects.all()
        serializer = SessionRegisterSerializer(session_registrations, many=True)
        return Response(serializer.data)
