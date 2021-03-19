from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FormParser, JSONParser
from core.models import User, UserProfile
from core.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all()

    def perform_create(self, serializer):
        return serializer.save(self.request.user)

    @action(permission_classes=[IsAuthenticated], detail=False)
    def me(self, request, *args, **kwargs):
        User = get_user_model()
        self.object = get_object_or_404(User, pk=request.user.id)
        serializer = self.get_serializer(self.object)
        return Response(serializer.data)