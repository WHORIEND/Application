from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MyUser
from .serializers import BaseUserSerializer,LoginUserSerializer
# Create your views here.


class CurUserAPI(generics.RetrieveAPIView):
    def get(self,request,*args, **kwargs): # get 으로 들어왔을때
        email = request.data['email']
        curUser = MyUser.objects.get(id=email)
        serializer = BaseUserSerializer(request.data)
        return Response(serializer.data)


class UserLoginAPI(generics.RetrieveAPIView): # login url로 들어옴

    def post(self, request, *args, **kwargs): #post로 들어왔을 때
        serializer = LoginUserSerializer(request.data)
        if serializer.validated_data['email'] == "None":
            return Response({'message': 'fail'}, status=status.HTTP_200_OK) #login 실패

        response = {
            'success': 'True',
            'token': serializer.data['token']
        }
        return Response(response, status=status.HTTP_200_OK) #login 성공
