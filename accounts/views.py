from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import ParentRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from main.models import User, Parent
from django.core.cache import cache


class ParentRegisterView(CreateView):
    model = User
    form_class = ParentRegistrationForm
    template_name = 'parent/parent_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main:home')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("sessionOOK", username)
                request.session['username'] = username
                user = User.objects.get(username=username)
                parent = Parent.objects.get(user_id=user.id)

                request.session['id_parent'] = parent.id
                print('AZZZAZAZAZAZA', parent.id)
                cache.set('id_parent', parent.id)

                return redirect('main:home')
            else:
                messages.error(request, "Invalid username or password")
        else:
            # messages.error(request,"Invalid username or password")
            AuthenticationForm()

    return render(request, 'login.html',
                  context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')
