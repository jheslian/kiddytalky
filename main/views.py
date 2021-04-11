from django.shortcuts import render, get_object_or_404
from main.models import Parent
from django.views.generic import DetailView
from crum import get_current_user


def home_view(request):
   #id_ = self.kwargs.get("id")
   #self.request.session['id_parent'] = id_
   #parent = Parent.objects.get(user_id=id_)
   #cache.set('parent_id', parent.id)
   e = get_current_user()
   print("HOME CRUMMMMMM", e.id)

   return render(request, 'main/home.html')


def index_view(request):
   return render(request, 'index.html')


class MyHomeView(DetailView):
   template_name = 'main/home.html'

   def get_object(self):
      id_parent = self.request.session['id_parent']

      print('id userparentAAAAAAAA: ', id_parent)
      #parent = Parent.objects.get(user_id=id_)


      return get_object_or_404(Parent, id=id_parent)




