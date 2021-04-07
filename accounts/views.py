from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from accounts.forms import ParentRegistrationForm
from django.views.generic import (CreateView, DetailView)
from accounts.forms import ParentRegistrationForm
from main.models import Parent
from django.contrib import messages

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


"""class ParentDetailView(DetailView):

    template_name = 'main/home.html'

    def get_object(self):
       id_ = self.kwargs.get("id")
       return get_object_or_404(Parent, id=id_)"""


class RegisterParentView(CreateView):
    template_name = 'parent/registration.html'
    form_class = ParentRegistrationForm
    queryset = Parent.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


def login_view(request):
    if request.method == 'POST':
        try:
            print("password", request.POST['password'])
            # password=request.POST['password']
            user = Parent.objects.get(email=request.POST['username'], password=request.POST['password'])
            #user = Parent.objects.get(email=request.POST['username'])
            print("email",request.POST['username'])
            print("userdetails", user)
            request.session['email']=user.email

            return render(request, 'main/home.html')
        except Parent.DoesNotExist:
            messages.success(request, 'Username / Password Invalid')
    return render(request, 'parent/login.html')


def logout_view(request):
    try:
        del request.session['email']
    except:
        return render(request, 'parent/login.html')

    #return render(request, 'parent/login.html')
    return redirect('main:accounts:login')


