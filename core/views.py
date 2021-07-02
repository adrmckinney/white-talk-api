from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FormParser, JSONParser
from core import serializers
from core.models import Announcement, User, SessionRegistrant, Session
# UserCreateSerializer
from core.serializers import AnnouncementSerializer, SessionRegisterSerializer, SessionSerializer, UserSerializer
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.mail import send_mail


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class LoggedInUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UpdateUserView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self, pk):
        user = self.request.user
        return user


class SessionRegisterView(ListCreateAPIView):
    queryset = SessionRegistrant.objects.all()
    serializer_class = SessionRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()

    def get(self, request):
        session_registrations = SessionRegistrant.objects.all()
        serializer = SessionRegisterSerializer(
            session_registrations, many=True)
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


class UpdateSessionRegistrant(UpdateAPIView):
    queryset = SessionRegistrant.objects.all()
    serializer_class = SessionRegisterSerializer

    def partial_update(self, request, pk):
        registrant = get_object_or_404(SessionRegistrant, pk=pk)

        registrant.update()
        serializer = SessionRegisterSerializer(registrant)
        return Response(serializer.data)


class CreateAnnouncement(ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get(self, request):
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(
            announcements, many=True)
        return Response(serializer.data)
