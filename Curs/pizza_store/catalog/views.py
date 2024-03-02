from django.shortcuts import render, redirect, reverse


def home_view(request):
    return render(request, 'home.html')