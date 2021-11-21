from django.urls import path
from .import views

app_name = "mainApp"

urlpatterns = [
    path("", views.mainView.as_view()),
    path("언어/", views.TeachableUserView),
    path("/login",views.login()),
    path("/logout",views.login()),
]