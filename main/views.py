from django.shortcuts import render, get_object_or_404
from main.models import Parent
from django.core.cache import cache
from django.views.generic import DetailView


def home_view(request):
   #id_ = self.kwargs.get("id")
   #self.request.session['id_parent'] = id_
   #parent = Parent.objects.get(user_id=id_)
   #cache.set('parent_id', parent.id)
   print("cacahe set home,", cache.get('parent_id'))

   return render(request, 'main/home.html')


def index_view(request):
   return render(request, 'index.html')


class MyHomeView(DetailView):
   template_name = 'main/home.html'

   def get_object(self):
      id_parent = self.request.session['id_parent']

      print('id userparentAAAAAAAA: ', id_parent)
      #parent = Parent.objects.get(user_id=id_)

      print("cachet get ",cache.get('id_parent'))
      return get_object_or_404(Parent, id=id_parent)







