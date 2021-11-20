from rest_framework import serializers
from .models import *

class DetailCategorySeralizer(serializers.ModelSerializer):
    class Meta:
        model = Detail_Category
        fields = ("category_name", "detail_name", "image")