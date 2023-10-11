from rest_framework import serializers

from articles.serializers import ArticleListSerializer
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    followers =serializers.StringRelatedField(many=True) 
    followings =serializers.StringRelatedField(many=True)
    # article_set = ArticleListSerializer(many=True)
    # like_articles = ArticleListSerializer(many=True)
    class Meta:
        model = User
        # fields = "__all__"
        fields = ("id","email","followings", "followers")




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
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