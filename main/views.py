from django.shortcuts import render, redirect
# from django.contrib.auth import logout

# Create your views here.
from django.shortcuts import render


def home(request):
   return render(request, 'main/home.html')


def conversation(request):
   return render(request, 'main/msg.html')


"""def get_absolute_url(request):
   return render(request, '/')"""