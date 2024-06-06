from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
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
    

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': str(e)})

