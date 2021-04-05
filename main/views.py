from django.shortcuts import render, redirect
# from django.contrib.auth import logout

# Create your views here.
from django.shortcuts import render

def home(request):
   return render(request, 'home.html')

