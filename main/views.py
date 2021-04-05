from django.shortcuts import render, redirect
# from django.contrib.auth import logout

def home(request):
    return render(request, 'main/home.html')



