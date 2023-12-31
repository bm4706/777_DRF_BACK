from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User

from users.serializers import UserProfileSerializer, UserSerializer, CustomTokenObtainPairSerializer

from rest_framework_simplejwt.views import (
    TokenObtainPairView, # 로그인기능?
    TokenRefreshView,
)

from rest_framework import permissions

from rest_framework.generics import get_object_or_404

from rest_framework.permissions import IsAuthenticated

# 회원가입
class Signup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

# 로그인
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

"""# 로그아웃
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # 현재 사용자의 토큰을 무효화하기 위해 토큰을 삭제합니다.
        request.auth.delete()
        return Response("로그아웃",status=status.HTTP_204_NO_CONTENT)"""
        

# 팔로우
class Follow_View(APIView):
    def post(self, request, user_id):
        you = get_object_or_404(User, id=user_id) # user id 가져오기
        me = request.user # 로그인 유저
        if me in you.followers.all():
            you.followers.remove(me)
            return Response("팔로우를 취소하였습니다.", status=status.HTTP_200_OK)
        else:
            you.followers.add(me)
            return Response("팔로우했습니다.", status=status.HTTP_200_OK)


# 프로필 확인!  
class ProfileView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)