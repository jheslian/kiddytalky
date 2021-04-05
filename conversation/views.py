from django.shortcuts import render


def conversation_view(request):
    return render(request, 'main/msg.html')

