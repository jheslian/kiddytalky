from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from accounts.forms import ParentRegistrationForm
from django.views.generic import (CreateView, DetailView)
from accounts.forms import ParentRegistrationForm
from main.models import Parent

"""def parent_registration_view(request):
    context = {}
    if request.POST:
        form = ParentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form

    else:
        form = ParentRegistrationForm()
        context['registration_form'] = form
    return render(request, 'parent/registration.html', context)
"""


class ParentDetailView(DetailView):

    """CHANGE TO GET FIRSTNAME ex:
    def get_first_name(self):
        return self.first_name

    """

    template_name = './home.html'

    def get_object(self):
       id_ = self.kwargs.get("id")
       return get_object_or_404(Parent, id=id_)


class RegisterParentView(CreateView):
    template_name = 'parent/registration.html'
    form_class = ParentRegistrationForm
    queryset = Parent.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


def login_view(request):
   return render(request, 'parent/login.html')