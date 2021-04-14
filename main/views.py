from django.shortcuts import render, get_object_or_404
from main.models import Parent
from django.views.generic import DetailView
from crum import get_current_user
import requests
import json
import http.client
from django.http import HttpResponseRedirect


def home_view(request):
    # id_ = self.kwargs.get("id")
    # self.request.session['id_parent'] = id_
    # parent = Parent.objects.get(user_id=id_)
    # cache.set('parent_id', parent.id)
    e = get_current_user()
    print("HOME CRUMMMMMM", e.id)

    return render(request, 'main/home.html')


def index_view(request):
    return render(request, 'index.html')


class MyHomeView(DetailView):
    template_name = 'main/home.html'

    def get_object(self):
        id_parent = self.request.session['id_parent']

        print('id userparentAAAAAAAA: ', id_parent)
        # parent = Parent.objects.get(user_id=id_)

        return get_object_or_404(Parent, id=id_parent)


"""def create_meeting(request):
    
    conn = http.client.HTTPSConnection("api.zoom.us")

    payload = "{\"topic\":\"API Test\",\"type\":\"1\",\"start_time\":\"2021-08-30T22:00:00Z\",\"duration\":\"60\",\"timezone\":\"America/New_York\",\"password\":\"password\",\"agenda\":\"Test de creation de meeting\",\"settings\":{\"host_video\":\"True\",\"participant_video\":\"True\",\"cn_meeting\":\"False\",\"in_meeting\":\"False\",\"join_before_host\":\"False\",\"mute_upon_entry\":\"False\",\"watermark\":\"False\",\"use_pmi\":\"False\",\"approval_type\":\"0\",\"audio\":\"0\",\"auto_recording\":\"none\",\"enforce_login\":\"False\",\"registrants_email_notification\":\"False\"}}"

    headers = {
        'authorization': "Bearer eyJhbGciOiJIUzUxMiIsInYiOiIyLjAiLCJraWQiOiJjYzhiNmFjZC1mNDc5LTRhNjMtYWY2My1jNDliNTRlNTA5MTAifQ.eyJ2ZXIiOjcsImF1aWQiOiIwNjYwNGNmZjIzM2YyMGExMjMzOGE1ZjU5YTMyNzkyNCIsImNvZGUiOiJuc3VHNDRTSnd1X0tUaEVoaGZNU2NlWFBDNEFYZjZsRnciLCJpc3MiOiJ6bTpjaWQ6ZldUNzI2YVNTS1NwOE5VSzh5YzY5ZyIsImdubyI6MCwidHlwZSI6MCwidGlkIjowLCJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJLVGhFaGhmTVNjZVhQQzRBWGY2bEZ3IiwibmJmIjoxNjE4MzUxNjE3LCJleHAiOjE2MTgzNTUyMTcsImlhdCI6MTYxODM1MTYxNywiYWlkIjoiZXo3R0ZuSDhUb1dvNUdUOWY0eDVxUSIsImp0aSI6ImVjZjYwNDgyLTAyNWItNDM3NS05ZWE3LTE3N2U3Yzc4NTA5MSJ9.tWuoO9T_JaoZpJkjFnEZ7eisAIwEUxgE-kfS89QIAci7fFfywjvt_AtzIbB68-my6AXx2JIXvxRdOZ7VqaJI9Q",
        'content-type': "application/json"
    }

    conn.request("POST", "/v2/users/justinjhes@gmail.com/meetings", payload, headers)
    data = json.load(conn.getresponse())

    # ZOOM JOIN URL
    print("THIS IS THE JOIN URL", data['join_url'])

    return HttpResponseRedirect('/')
    """


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




