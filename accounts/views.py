from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import ParentRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from main.models import User


class ParentRegisterView(CreateView):
    model = User
    form_class = ParentRegistrationForm
    template_name = 'parent/parent_register.html'

    def form_valid(self, form):
        form.save()
        #user = form.save()
        #login(self.request, user)
        #self.request.session['username'] = user.username
        return redirect('main:login')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                #request.session['id_parent'] = user.id
                #request.session['id_child_app'] = user.id


                if user.is_parent:
                    request.session['id_parent'] = user.id
                    print(request.session['id_parent'])
                    return redirect('main:home')
                else:
                    request.session['id_child_app'] = user.id
                    print("CHILD APP SESSION ID",  request.session['id_child_app'])
                    return redirect('child_account:child-home')

            else:
                messages.error(request, "Invalid username or password")
        else:
            AuthenticationForm()

    return render(request, 'login.html',
                  context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('/')


def get_meeting(request):

    """
    data = requests.post{"https:/api.zoom.us/v2/users/{email}/meetings",
        headers={"content-type": "application/json",
        "authorization": f"Bearer {request.session['zoom-access-token]}"
        },
    data = json.dumps({
        "topic": "interview with",
        "type": 2,
        "start": "2020-04-15T10:00:00"
    })
    """

    pass