from django.shortcuts import render, redirect, get_object_or_404
from .models import Parent, Child, Languagetolearn, Language
from django.views.generic import DetailView, ListView, UpdateView
from crum import get_current_user
from mykids.formplanning import EventForm
import requests
import json
import http.client
from .forms import MeetingValidationForm
from django.http import HttpResponseRedirect
from mykids.forms import EditChildInfo


def index_view(request):
    return render(request, 'index.html')


"""
def home_view(request):
    # id_ = self.kwargs.get("id")
    # self.request.session['id_parent'] = id_
    # parent = Parent.objects.get(user_id=id_)
    # cache.set('parent_id', parent.id)
    #request.session['correspondent_id']
    e = get_current_user()
    print("HOME CRUMMMMMM", e.id)

    return render(request, 'main/home.html')"""


class CorrespondentListView(ListView):
    template_name = 'main/home.html'
    queryset = Child.objects.all()


class MeetingValidationView(ListView):
    model = Languagetolearn
    template_name = 'main/correspondent-detail.html'
    success_url = '/home'

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context = super(CorrespondentDetailView, self).get_context_data(**kwargs)
        id_ = self.kwargs.get('id')
        print("GETCONTEXT ID", id_)


        context = super(MeetingValidationView, self).get_context_data(**kwargs)

        # this are the proposition of a child
        context['proposition'] = Languagetolearn.objects.filter(child_id=id_, validation_status='Pending')

        # option for the select which contains the kids who will accept the proposition
        user = get_current_user().id
        parent = Parent.objects.get(user_id=user)
        option = Child.objects.filter(parent_id=parent.id)
        context['select_child'] = option

        # this are the details the child
        child = Child.objects.filter(id=id_)
        context['child_data'] = child

        """ child_lang = Languagetolearn.objects.filter(child_id=id_)

        proposed_language = Language.objects.filter(id=child_lang.language_id)
        print("HGDGNFFNDS", proposed_language)
        context['language_proposed'] = proposed_language"""
        return context


    """class AcceptEvent(UpdateView):
    print('the proposition id', id)
    # id_ = self.kwargs.get("id")
    test = request.GET.get('option', None)

    print("ID CHILD", id_child)
    print("ID EVENT", id_event)
    print("the select value", test)
    
    template_name = 'main/correspondent-detail.html'
    form_class = MeetingValidationForm
    queryset = Languagetolearn.objects.all()
    #success_url = f"/{id}"

    def form_valid(self, form,):

        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Languagetolearn, id=id_)



    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)


    #id_ = request.session['child_id']
    #print('ZZZZZZZZZZ', id_)
    # Languagetolearn.objects.get(id=id_event).delete()
    Languagetolearn.objects.filter(id=id).update(validation_status='Confirmed' )
    # correspondent_language_id=1
    # child_correspondent_id = id,"""

    # return redirect(f"/{id}")



def accept_event(request,id_child, id_event):
    #print('SELECT CHILD ID', id)
    correspondent_id = request.GET.get('option', None)

    print("ID CHILD who proposed", id_child)
    print("ID EVENT", id_event)
    print("the select valueGGGGG", correspondent_id)

    language = Child.objects.get(id=id_child)
    print("Child langID", language.id)

    Languagetolearn.objects.filter(id=id_event).update(validation_status='Confirmed', child_correspondent_id=correspondent_id, correspondent_language_id=language.language_id)

    print("buttona accept")


    return redirect(f"/{id_child}")


def create_meeting(request):
    conn = http.client.HTTPSConnection("api.zoom.us")

    payload = "{\"topic\":\"API Test\",\"type\":\"1\",\"start_time\":\"2019-08-30T22:00:00Z\",\"duration\":\"60\",\"timezone\":\"America/New_York\",\"password\":\"password\",\"agenda\":\"Test de creation de meeting\",\"settings\":{\"host_video\":\"True\",\"participant_video\":\"True\",\"cn_meeting\":\"False\",\"in_meeting\":\"False\",\"join_before_host\":\"False\",\"mute_upon_entry\":\"False\",\"watermark\":\"False\",\"use_pmi\":\"False\",\"approval_type\":\"0\",\"audio\":\"0\",\"auto_recording\":\"none\",\"enforce_login\":\"False\",\"registrants_email_notification\":\"False\"}}"

    headers = {
        'content-type': "application/json",
        'authorization': "Bearer eyJhbGciOiJIUzUxMiIsInYiOiIyLjAiLCJraWQiOiI1ZGUyOTNiNS0wOWM1LTQ5OGMtYjY3Mi0yMmQwN2VlZDFmZTUifQ.eyJ2ZXIiOjcsImF1aWQiOiIwNjYwNGNmZjIzM2YyMGExMjMzOGE1ZjU5YTMyNzkyNCIsImNvZGUiOiJNTTFlaW50MkwzX0tUaEVoaGZNU2NlWFBDNEFYZjZsRnciLCJpc3MiOiJ6bTpjaWQ6ZldUNzI2YVNTS1NwOE5VSzh5YzY5ZyIsImdubyI6MCwidHlwZSI6MCwidGlkIjowLCJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJLVGhFaGhmTVNjZVhQQzRBWGY2bEZ3IiwibmJmIjoxNjE4NDAzOTE4LCJleHAiOjE2MTg0MDc1MTgsImlhdCI6MTYxODQwMzkxOCwiYWlkIjoiZXo3R0ZuSDhUb1dvNUdUOWY0eDVxUSIsImp0aSI6ImU0Mzk3MzU0LWZmMmUtNDhjNC1iZjMxLWFhMTlkMmU3YjI3NCJ9.TaovSuBoASYvO5lpjECIGBXI4Cwjl_vFofTd_5Lei8yJmYBvbWlZOEcX248zNJFndJQ06ibAW1rEFW7uxUSPwg"
    }

    conn.request("POST", "/v2/users/justinjhes@gmail.com/meetings", payload, headers)
    data = json.load(conn.getresponse())

    # ZOOM JOIN URL
    print("THIS IS THE JOIN URL", data['join_url'])

    return HttpResponseRedirect('/')


"""def get_meeting(request):
    conn = http.client.HTTPSConnection("api.zoom.us")
    headers = {
        'authorization': "Bearer eyJhbGciOiJIUzUxMiIsInYiOiIyLjAiLCJraWQiOiJjYzhiNmFjZC1mNDc5LTRhNjMtYWY2My1jNDliNTRlNTA5MTAifQ.eyJ2ZXIiOjcsImF1aWQiOiIwNjYwNGNmZjIzM2YyMGExMjMzOGE1ZjU5YTMyNzkyNCIsImNvZGUiOiJuc3VHNDRTSnd1X0tUaEVoaGZNU2NlWFBDNEFYZjZsRnciLCJpc3MiOiJ6bTpjaWQ6ZldUNzI2YVNTS1NwOE5VSzh5YzY5ZyIsImdubyI6MCwidHlwZSI6MCwidGlkIjowLCJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJLVGhFaGhmTVNjZVhQQzRBWGY2bEZ3IiwibmJmIjoxNjE4MzUxNjE3LCJleHAiOjE2MTgzNTUyMTcsImlhdCI6MTYxODM1MTYxNywiYWlkIjoiZXo3R0ZuSDhUb1dvNUdUOWY0eDVxUSIsImp0aSI6ImVjZjYwNDgyLTAyNWItNDM3NS05ZWE3LTE3N2U3Yzc4NTA5MSJ9.tWuoO9T_JaoZpJkjFnEZ7eisAIwEUxgE-kfS89QIAci7fFfywjvt_AtzIbB68-my6AXx2JIXvxRdOZ7VqaJI9Q"}

    conn.request("GET", "/v2/meetings/7786931907", headers=headers)

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    #print("THIS IS THE GET METTING", res)

    return HttpResponseRedirect('/')"""
