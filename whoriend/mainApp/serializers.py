from rest_framework import serializers
from .models import *

class DetailCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail_Category
        fields = ["category_name", "detail_name", "image"]

class TeachableUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["nickname", "gender", "image"]