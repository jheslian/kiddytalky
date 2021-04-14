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
    """url = "https://api.zoom.us/v2/meetings/7786931907"

    headers = {
        'authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInYiOiIyLjAiLCJraWQiOiI2YTNkMTAzMy1iNTk1LTQ4YTYtOGQ4MC0yNmFhOTY2NzVhOWQifQ.eyJ2ZXIiOjcsImF1aWQiOiIwNjYwNGNmZjIzM2YyMGExMjMzOGE1ZjU5YTMyNzkyNCIsImNvZGUiOiJMM1FualYwMEI4X0tUaEVoaGZNU2NlWFBDNEFYZjZsRnciLCJpc3MiOiJ6bTpjaWQ6ZldUNzI2YVNTS1NwOE5VSzh5YzY5ZyIsImdubyI6MCwidHlwZSI6MCwidGlkIjowLCJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJLVGhFaGhmTVNjZVhQQzRBWGY2bEZ3IiwibmJmIjoxNjE4MzI5OTc4LCJleHAiOjE2MTgzMzM1NzgsImlhdCI6MTYxODMyOTk3OCwiYWlkIjoiZXo3R0ZuSDhUb1dvNUdUOWY0eDVxUSIsImp0aSI6IjQ0Yzk1NzI0LTAwODktNDg1YS05NWQyLTZiY2VkYzU3ZmM0YSJ9.nc-8v0deNHEmGo4DUw2EDfyCwZNgjKgPLx0R4Wc-y_ihyYS7lXNXOGFqp2r0Kk2ridY4UL36cIVdm0QXGXMeeA'}

    response = request("GET", url, headers=headers)

    print(response.text)"""





    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                request.session['id_parent'] = user.id

                if user.is_parent:
                    return redirect('main:home')
                #else:
                    #return redirect('main:kids_accounts')

            else:
                messages.error(request, "Invalid username or password")
        else:
            AuthenticationForm()

    return render(request, 'login.html',
                  context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
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