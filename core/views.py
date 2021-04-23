from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FormParser, JSONParser
from core import serializers
from core.models import User, SessionRegistrant, Session
from core.serializers import UserSerializer, SessionRegisterSerializer, SessionSerializer
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        # takes all the user info and turns it into JSON
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class LoggedInUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(data=serializer.data)

class SessionRegisterView(ListCreateAPIView):
    queryset = SessionRegistrant.objects.all()
    serializer_class = SessionRegisterSerializer
    permission_classes = [permissions.AllowAny]
    def perform_create(self, serializer):

        # local email set up with personal gmail account
        # template = render_to_string('base/email_template.html', 
        #                             {
        #                                 'first_name': serializer.validated_data["first_name"]
        #                             })
        # email = EmailMessage(
        #     'test email from Django',
        #     template,
        #     settings.EMAIL_HOST_USER,
        #     ['adrmckinney@icloud.com'],
        #     [serializer.validated_data["email"]]
        # )
        # email.fail_silently = False
        # email.send()
        
        serializer.save()
    
    # This is for mailgun on heroku. Not sure where it goes.
    # def send_simple_message():
    #     return requests.post(
    #         "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
    #         auth=("api", "YOUR_API_KEY"),
    #         data={"from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
    #             "to": ["bar@example.com", "YOU@YOUR_DOMAIN_NAME"],
    #             "subject": "Hello",
    #             "text": "Testing some Mailgun awesomness!"})

    def get(self, request):
        session_registrations = SessionRegistrant.objects.all()
        serializer = SessionRegisterSerializer(session_registrations, many=True)
        return Response(serializer.data)

class CreateSession(CreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class Sessions(ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

class DeleteSession(DestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def delete(self, request, pk):
        session = get_object_or_404(Session, pk=pk)

        session.delete()
        serializer = SessionSerializer(session)
        return Response(serializer.data)

class UpdateSession(UpdateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def partial_update(self, request, pk):
        session = get_object_or_404(Session, pk=pk)

        session.update()
        serializer = SessionSerializer(session)
        return Response(serializer.data)

class DeleteSessionRegistrant(DestroyAPIView):
    queryset = SessionRegistrant.objects.all()
    serializer_class = SessionRegisterSerializer

    def delete(self, request, pk):
        registrant = get_object_or_404(SessionRegistrant, pk=pk)

        registrant.delete()
        serializer = SessionRegisterSerializer(registrant)
        return Response(serializer.data)