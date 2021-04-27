from django.shortcuts import render


def login(request):
    return render(request, "loginPage.html")


def registration(request):
    return render(request, "registration.html")