from rest_framework import serializers
from .models import MyUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields="__all__"
        
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer): # 토큰 방식의 로그인
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        
        return token