from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User

from users.serializers import CustomTokenObtainPairSerializer, UserSerializer, UserProfileSerializer

from rest_framework_simplejwt.views import (
    TokenObtainPairView, # 로그인기능?
    TokenRefreshView,
)

from rest_framework import permissions

from rest_framework.generics import get_object_or_404


# 회원가입
class Signup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.save()
        return Response({"message": "가입완료!"}, status=status.HTTP_201_CREATED)

# 로그인