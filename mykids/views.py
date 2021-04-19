from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import UpdateView, DetailView, DeleteView, CreateView, ListView, FormView
from .forms import EditChildInfo, ChildRegistrationForm
from main.models import Child, User, Parent, Languagetolearn

from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from main.models import *
from .formplanning import EventForm
import json
import http.client
from dotenv import load_dotenv, dotenv_values
from datetime import datetime, timedelta
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView

from .utils import Calendar
from .formplanning import EventForm, SendMessage
from crum import get_current_user

def child_list_view(request):
    user_id = request.session['id_parent']
    parent = Parent.objects.get(user_id=user_id)
    queryset = Child.objects.filter(parent_id=parent.id)


    context = {
        "object_list": queryset
    }
    return render(request, 'mykids.html', context)


class MyChildView(DetailView):
    template_name = 'childview.html'

    def get_object(self):
        id_ = self.kwargs.get("id")

        self.request.session['child_id'] = id_
        print("CHILDVIEW IDDDDD", id_)
        return get_object_or_404(Child, id=id_)


class UpdateChildView(UpdateView):
    form_class = EditChildInfo
    template_name = 'editprofile_enfant.html'
    success_url = '/mykids'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")

        # Languagetolearn.objects.filter('language__language_choices'=)
        return get_object_or_404(Child, id=id_)


class DeleteChildView(DeleteView):
    template_name = 'child/delete.html'
    success_url = '/mykids'

    def get_object(self):
        id_ = self.kwargs.get("id")
        child = Child.objects.get(id=id_)
        print("OOOOODIDIIDID", child.user_id)
        return get_object_or_404(User, id=child.user_id)


class ChildRegisterView(CreateView):
    model = User
    form_class = ChildRegistrationForm
    template_name = 'child/child_register.html'

    def form_valid(self, form):
        form.save()
        return redirect('main:mykids:kids')


# --------------------------------------------------------------------------
# --------------------- delete event in message table-------------------------
def deletevent(request, id_event):
    print(id_event)
    # id_ = self.kwargs.get("id")
    id_ = request.session['child_id']
    print('ZZZZZZZZZZ', id_)
    Languagetolearn.objects.get(id=id_event).delete()

    return redirect(f"/mykids/{id_}/planning")


# ----------------------- show all event in planning view ---------------------
class planning_view(FormView, generic.ListView):
    model = Languagetolearn
    form_class = EventForm
    #template_name = 'planning.html'
    template_name = 'mykids.html'

    def post(self, request, *args, **kwargs):

        id_ = self.kwargs.get("id")
        self.request.session['child_id'] = id_
        if datetime.strptime(request.POST['date_slot'], "%Y-%m-%d") < datetime.today():
            messages.error(request, 'the date must be greater than today')
        elif request.POST['start_time_slot'] > request.POST['end_time_slot']:
            messages.error(request, 'start date must be less than the end date ')

        else:

            conn = http.client.HTTPSConnection("api.zoom.us")

            date_input = request.POST['date_slot']
            start_time = request.POST['start_time_slot']
            end_time = request.POST['end_time_slot']

            fmt = '%H:%M'
            start_timestamp = datetime.strptime(start_time, fmt)
            print("00000")
            end_timestamp = datetime.strptime(end_time, fmt)
            print("Start: ", start_timestamp)
            print("End: ", end_timestamp)
            print("YYY",end_timestamp.time(), start_timestamp.time())
            calcul = end_timestamp - start_timestamp
            calcul = str(calcul)


            delta = timedelta(hours=int(calcul.split(':')[0]), minutes=int(calcul.split(':')[1]), seconds=int(calcul.split(':')[2]))
            minutes = int(delta.total_seconds() / 60)
            print(minutes)

            print("DURATION", minutes)



            payload = "{\"topic\":\"API Test\",\"type\":\"2\",\"start_time\":\"+"+str(date_input)+"T"+str(start_time)+"Z\",\"duration\":\""+str(minutes)+"\",\"timezone\":\"America/New_York\",\"password\":\"password\",\"agenda\":\"Test de creation de meeting\",\"settings\":{\"host_video\":\"True\",\"participant_video\":\"True\",\"cn_meeting\":\"False\",\"in_meeting\":\"False\",\"join_before_host\":\"True\",\"mute_upon_entry\":\"False\",\"watermark\":\"False\",\"use_pmi\":\"False\",\"approval_type\":\"0\",\"audio\":\"0\",\"auto_recording\":\"none\",\"enforce_login\":\"False\",\"registrants_email_notification\":\"False\"}}"
            envdict = dotenv_values('.env')

            print('EEEEE', payload)

            headers = {
                'content-type': "application/json",
                'authorization': envdict["TOKEN_URL"]
            }

            conn.request("POST", "/v2/users/justinjhes@gmail.com/meetings", payload, headers)
            data = json.load(conn.getresponse())

            # ZOOM JOIN URL
            print('TOKEN',load_dotenv('TOKEN_URL'))

            Languagetolearn(language_id=request.POST['language'], start_time_slot=request.POST['start_time_slot'],
                            end_time_slot=request.POST['end_time_slot'], child_id=id_,
                            date_slot=request.POST['date_slot'], meeting_id=data['id'], link_video=data['join_url']).save()
        #rqt = Languagetolearn.objects.filter(last_name_id=id_)

        #return redirect(f"/mykids/{id_}/planning", {'form': EventForm})

        return redirect(f"/mykids", {'form': EventForm})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['rqt'] = Languagetolearn.objects.filter(child_id=self.request.session['child_id'])

        # context['deleteEvent'] = delete_event(request, id_event=self.kwargs.get("id_event"))
        return context


class ChildPasswordChangeView(PasswordChangeView):
    template_name = 'parent/change_pass_parent.html'
    success_url = reverse_lazy('main:mykids:child-password-success')



class ChildPasswordDoneView(PasswordResetDoneView):
    template_name = 'child/change_pass_child_success.html'




# --------------------------------------------------------------------------
# -----------------  send a first message-----------------------------------



def sendmessage(request):
    # ------------ used to redirect ---------------
    id_ = request.session['child_id']
    # -------------------- id child : proposition---------------------
    id_child_annonce = 1
    # ------------------------ current user  id-----------------------
    parent = Parent.objects.get(user=request.session['id_parent'])
    from_id = parent.id
    # -----------------------------------------------------------------
    if request.method == 'POST':
        Message(content=request.POST['content'], child_id=id_child_annonce, message_from_id=from_id,
                message_to_id=2).save()

    return redirect(f"/mykids/{id_}")

