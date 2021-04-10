from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import UpdateView, DetailView, DeleteView, CreateView
from .forms import EditChildInfo, ChildRegistrationForm
from main.models import Child, User


class MyChildView(DetailView):
    template_name = 'mykids.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User, id=id_)

def mykid_view(request):
   return render(request, 'mykids.html')

"""
class UpdateChildView(UpdateView):
    form_class = EditChildInfo
    template_name = 'parent/editprofile_parent.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Child, user_id=id_)

    def get_success_url(self):
        return reverse('main:home')


class DeleteChildView(DeleteView):
    model = Child
    template_name = 'delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Child, user_id=id_)

    def get_success_url(self):
        return redirect('myaccounts:my-account') """


class ChildRegisterView(CreateView):
    model = User
    form_class = ChildRegistrationForm
    template_name = 'child/child_register.html'

    def form_valid(self, form):
        form.save()
        return redirect('main:mykids:childregister')