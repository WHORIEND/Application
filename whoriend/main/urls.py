from django.urls import path
from category import views as Category_View

app_name = "main"

urlpatterns = [path("", Category_View.CategoryView.as_view(), name = "category")]