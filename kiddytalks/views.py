
from django.shortcuts import render


def previous_session_view(request):
    return render(request, 'previous_session.html')

