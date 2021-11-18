from django.shortcuts import render
from django.views.generic import ListView, View
from django.http import HttpResponse
from .models import Category, Detail_Category

# Create your views here.

name = "Category"

class CategoryView(ListView):
    model = Category
    paginated_by = 4 #한 페이지에 4개씩
    paginated_orphans = 0 #남은 페이지들은 새로운 페이지에
    context_object_name = "category"
    ordering = "created"
    template_name = "folder/category_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for edge in context['category']:
            print(edge.name)
            context[edge.name] = Detail_Category.objects.filter(category_name__name=edge.name)
            for a in context[edge.name]:
                print(edge.name, "-", a.detail_name)

        return context


#class DetailCategoryView(ListView):
#    model = Detail_Category #각 카테고리별 사람 정보 보여주기
#    paginated_by = 4 #한 페이지에 4개씩 보여주기
#    paginated_orphans = 0
#    context_object_name = "detail_category"
    #ordering = [] #별점순으로 보여주기
