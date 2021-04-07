from django.shortcuts import render
from django.shortcuts import render, redirect
from main.models import Languagetolearn

from .formplanning import FormPlanning


def mykid_view(request):
   return render(request, 'mykids.html')


def planning_view(request):
   if request.method == "POST":
      form = FormPlanning(request.POST)
      if form.is_valid():
         form.save()
         return redirect('/planning')
   else:
      form = FormPlanning()
   return render(request, 'planning.html', {'form': form, 'data_planning': Languagetolearn.objects.all()})