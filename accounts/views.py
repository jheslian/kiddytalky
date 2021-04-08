from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from accounts.forms import ParentRegistrationForm
from django.views.generic import (CreateView, DetailView)
from accounts.forms import ParentRegistrationForm
from main.models import Parent
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from main.models import User

def register(request):
    return render(request, 'registration/register.html')
    # html parent vs child btn

class parent_register(CreateView):
    model = User
    form_class = ParentRegistrationForm
    template_name = 'parent/parent_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main:home')


class child_register(CreateView):
    model = User
    form_class = ChildRegistrationForm
    template_name = 'child/child_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main:home')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('main:home')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'login.html',
                  context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')


"""
def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def register_parent(request):
    if request.method == 'POST':
        form = ParentRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            form.cleaned_data['username']
            return redirect('accounts:login')
    else:
        form = ParentRegistrationForm

    context = {'form': form}
    return render(request, 'registration/register.html', context)
"""