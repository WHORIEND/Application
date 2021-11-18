from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import MyUser


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'name')


class LoginUserSerializer(serializers.Serializer): #로그인 기능
    userEmail = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)#DB에 저장된 로그인 정보 조회
        if user is not None: # login 성공
            return user
        else:
            return {
                'email': 'None'
            }