from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from accounts.forms import ParentRegistrationForm
from django.views.generic import (CreateView, DetailView)
from accounts.forms import ParentRegistrationForm
from main.models import Parent
from django.contrib import messages
from django.contrib.auth import logout


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
