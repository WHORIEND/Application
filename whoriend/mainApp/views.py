from django.shortcuts import render
from rest_framework.generics import *
from .serializers import *
from .models import *
# Create your views here.

class mainView(ListAPIView):
    queryset = Detail_Category.objects.all()
    serializer_class = DetailCategorySeralizer