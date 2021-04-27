from django.urls import path
from . import views

urlpatterns = [
    path("loginPage/", views.login, name="loginPage"),
    path("registration/", views.login, name="registration"),
]