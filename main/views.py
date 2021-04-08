from django.shortcuts import render


def home(request):
   return render(request, 'main/home.html')


def index_view(request):
   return render(request, 'index.html')





