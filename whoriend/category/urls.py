from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = "category"

URLPattern = [
    path("<int:pk>/", views.DetailCategoryView.as_view(), name = "Category"),
]