from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import *
app_name="backend"
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', CustomUserRegisterView.as_view(), name='register-user'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]