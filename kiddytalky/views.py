from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


# THIS NEEDS TO BE REMOVE