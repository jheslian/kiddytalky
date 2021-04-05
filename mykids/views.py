from django.shortcuts import render


def mykid_view(request):
   return render(request, 'mykids.html')
