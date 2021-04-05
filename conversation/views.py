from django.shortcuts import render


def conversation(request):
    return render(request, 'msg.html')

