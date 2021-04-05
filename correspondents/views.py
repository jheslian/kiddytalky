from django.shortcuts import render


def correspondent_view(request):
    return render(request, 'correspondent.html')