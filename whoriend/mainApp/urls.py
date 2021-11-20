from django.urls import path
from .import views

app_name = "mainApp"

urlpatterns = [
    path("", views.mainView.as_view()),
]