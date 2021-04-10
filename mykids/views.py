from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import UpdateView, DetailView, DeleteView, CreateView, ListView
from .forms import EditChildInfo, ChildRegistrationForm
from main.models import Child, User


class ChildListView(ListView):
   template_name = 'mykids.html'
   queryset = Child.objects.all().filter(parent_id=2)
   #queryset = Child.objects.all()


class MyChildView(DetailView):
    template_name = 'childview.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Child, id=id_)


class UpdateChildView(UpdateView):
    form_class = EditChildInfo
    template_name = 'editprofile_enfant.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Child, id=id_)

    def get_success_url(self):
        return reverse('main:mykids:kids')


class DeleteChildView(DeleteView):
    model = Child
    template_name = 'delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Child, user_id=id_)

    def get_success_url(self):
        return redirect('main:mykids:kids')


class ChildRegisterView(CreateView):
    model = User
    form_class = ChildRegistrationForm
    template_name = 'child/child_register.html'

    def form_valid(self, form):
        form.save()
        return redirect('main:mykids:childregister')