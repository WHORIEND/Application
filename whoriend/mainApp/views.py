import json
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

class mainView(ListAPIView):
    queryset = Detail_Category.objects.all()
    serializer_class = DetailCategorySerializer

@api_view(['GET'])
def TeachableUserView(request):
    print('hello')
    if request == 'GET':
        #data = json.loads(request.body)
        #category = data['category']
        category = '언어'
        queryset = User.objects.filter(interest__category_name = category) #json형식으로 받은 카테고리만 걸러서 리턴
        serializers = TeachableUserSerializer(queryset)
        #context = {"result" : queryset}
        return Response(serializers)