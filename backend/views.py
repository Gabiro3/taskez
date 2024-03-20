from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.response import Response
from .serializers import *
# Create your views here.
class CustomUserRegisterView(generics.CreateAPIView):

    model = get_user_model()
    serializer_class = UserRegisterSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data)
        username = ""
        if serializer.is_valid():
           username = serializer.validated_data.get('email')
        return Response(status=status.HTTP_201_CREATED)

