from django.shortcuts import render, redirect, get_object_or_404
from .models import Parent, Child, Languagetolearn, Language, Country
from django.views.generic import DetailView, ListView, UpdateView
from crum import get_current_user
import json
import http.client

from django.http import HttpResponseRedirect


def index_view(request):
    return render(request, 'index.html')


"""class CorrespondentListView(ListView):
    template_name = 'main/home.html'
    queryset = Child.objects.all()"""


def correspondent_list_view(request):
    country = Country.objects.all()
    language = Language.objects.all()

    language_option = request.GET.get('language')
    print("lang", language)

    country_option = request.GET.get('country')
    print("count", country)


    if country_option and language_option:
        queryset = Child.objects.filter(country_id=country_option, language_id=language_option)
    elif country_option:
        queryset = Child.objects.filter(country_id=country_option)
    elif language_option:
        queryset = Child.objects.filter(language_id=language_option)
    else:
        queryset = Child.objects.all()
    


    context = {
        "object_list": queryset,
        "option_country": country,
        "option_laguage": language
    }
    return render(request, 'main/home.html', context)


class MeetingValidationView(ListView):
    model = Languagetolearn
    template_name = 'main/correspondent-detail.html'

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

        return context


def accept_event(request, id_child, id_event):
    # print('SELECT CHILD ID', id)
    correspondent_id = request.GET.get('option', None)

    print("ID CHILD who proposed", id_child)
    print("ID EVENT", id_event)
    print("the select valueGGGGG", correspondent_id)

    language = Child.objects.get(id=id_child)
    print("Child langID", language.id)

    Languagetolearn.objects.filter(id=id_event).update(validation_status='Confirmed',
                                                       child_correspondent_id=correspondent_id,
                                                       correspondent_language_id=language.language_id)

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
