from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FormParser, JSONParser
from core import serializers
from core.models import User, SessionRegister
from core.serializers import UserSerializer

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        # takes all the user info and turns it into JSON
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# class SessionRegister(ListCreateAPIView):
