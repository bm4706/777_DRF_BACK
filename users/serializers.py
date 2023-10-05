from rest_framework import serializers
from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields="__all__"
        
        
    def create_user(self):
        user = super().create() # Modelserializer 에서 참조
        password = user.password
        nickname = user.nickname
        user.set_password(password) # 비밀번호 해싱
        user.save()
        return user
    