import json
from django.db.models import query
from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializers import *
from .models import *
# Create your views here.

class mainView(APIView):
    def get(self, request):
        queryset = Detail_Category.objects.all()
        serializers = DetailCategorySerializer(queryset, many=True)
        return Response(serializers.data)

class TeachableUserView(APIView):
    def get(self, request):
        queryset = User.objects.filter(interest__name__in = ['언어']) #json형식으로 받은 카테고리만 걸러서 리턴
        for e in queryset:
            print(e)
        serializers = TeachableUserSerializer(queryset, many=True)
        #context = {"result" : queryset}
        return Response(serializers.data)

#@api_view(['GET'])
#def TeachableUserView(request):
#    print('hello')
#    if request == 'GET':
#        #data = json.loads(request.body)
#        #category = data['category']
#        category = '언어'
#        queryset = User.objects.filter(interest__category_name = category) #json형식으로 받은 카테고리만 걸러서 리턴
#        serializers = TeachableUserSerializer(queryset)
#        #context = {"result" : queryset}
#        return Response(serializers.data)