from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import UpdateView, DeleteView, DetailView
from main.models import Parent, User
from .forms import EditParentInfo
from accounts.forms import ParentRegistrationForm


def my_account_view(request):
    return render(request, 'myAccount.html')


class MyAccountView(DetailView):
    template_name = 'myAccount.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User, id=id_)


class UpdateParentView(UpdateView):
    form_class = EditParentInfo
    template_name = 'parent/edit_profile.html'
    # queryset = Parent.objects.all()


    def form_valid(self, form):
        #user = super().save(commit=False)
        """User.first_name = self.cleaned_data.get('first_name')
        User.last_name = self.cleaned_data.get('last_name')
        User.birthdate = self.cleaned_data.get('birthdate')
        User.save()
        parent = Parent.objects.filter(user_id=id)
        parent.email = self.cleaned_data.get('email')
        parent.zipcode = self.cleaned_data.get('zipcode')
        parent.street = self.cleaned_data.get('street')
        parent.country = self.cleaned_data.get('country')
        parent.save()"""


        return super().form_valid(form)
        #return user


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Parent, id=id_)

    def get_success_url(self):
        return reverse('main:home')


class DeleteParentView(DeleteView):
    template_name = 'parent/edit_profile.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Parent, user_id=id_)

    def get_success_url(self):
        return redirect('index')
