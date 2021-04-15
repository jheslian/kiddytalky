from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import UpdateView, DetailView, DeleteView, CreateView, ListView, FormView
from .forms import EditChildInfo, ChildRegistrationForm
from main.models import Child, User, Parent, Languagetolearn
from django.core.cache import cache
from datetime import datetime, date, timedelta
import datetime as dt
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, request
from django.views import generic
from django.utils.safestring import mark_safe
import calendar
from django.urls import reverse_lazy
from main.models import *
from .utils import Calendar
from .formplanning import EventForm
import json
import http.client
from dotenv import load_dotenv, dotenv_values
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta


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
        """print('id user: ', id_)
        parent = Parent.objects.get(user_id=id_)
        print('Objet user: ', parent)
        print("id du parent: ", parent.id)"""
        # Child.parent_id = parent.id
        #  child = Child.objects.create(parent_id=parent.id)
        # child = Child.parent_id
        # print("child object",child)
        # child.save()

    """ def get_context_data(self):
        context = super().get_context_data()
        id_ = self.request.session['id_parent']
        parent = Parent.objects.get(user_id=id_)
        child = self.request.child
        context["parent_id"] = parent.objects.all()
        return context"""


# -------------------------------------------------
# -------------------------------------------------
"""
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
"""


# -------------------------------------------------
# -------------------------------------------------
def deletevent(request, id_event):
    print(id_event)
    #id_ = self.kwargs.get("id")
    id_ =request.session['child_id']
    print('ZZZZZZZZZZ', id_)
    Languagetolearn.objects.get(id=id_event).delete()

    return redirect(f"/mykids/{id_}/planning")


class planning_view(FormView, generic.ListView):
    model = Languagetolearn
    form_class = EventForm
    template_name = 'planning.html'

    def post(self, request, *args, **kwargs):

        id_ = self.kwargs.get("id")
        self.request.session['child_id'] = id_
        if datetime.strptime(request.POST['date_slot'], "%Y-%m-%d") < datetime.today():
            messages.error(request, 'the date must be greater than today')
        elif request.POST['start_time_slot'] >= request.POST['end_time_slot']:
            messages.error(request, 'start date must be less than the end date ')

        else:

            conn = http.client.HTTPSConnection("api.zoom.us")


            date_input = request.POST['date_slot']
            start_time = request.POST['start_time_slot']
            end_time = request.POST['end_time_slot']
            #duration_time = end_time - start_time

            fmt = '%H:%M'
            start_timestamp = datetime.strptime(start_time, fmt)
            print("00000")
            end_timestamp = datetime.strptime(end_time, fmt)
            print("Start: ", start_timestamp)
            print("End: ", end_timestamp)
            # duration = timedelta(end_timestamp.time()-start_timestamp.time())
            print("YYY",end_timestamp.time(), start_timestamp.time())
            calcul = end_timestamp - start_timestamp
            calcul = str(calcul)


            delta = timedelta(hours=int(calcul.split(':')[0]), minutes=int(calcul.split(':')[1]), seconds=int(calcul.split(':')[2]))
            minutes = int(delta.total_seconds() / 60)
            print(minutes)

            print("DURATION",minutes)



            payload = "{\"topic\":\"API Test\",\"type\":\"1\",\"start_time\":\"+"+str(date_input)+"T"+str(start_time)+"Z\",\"duration\":\""+str(minutes)+"\",\"timezone\":\"America/New_York\",\"password\":\"password\",\"agenda\":\"Test de creation de meeting\",\"settings\":{\"host_video\":\"True\",\"participant_video\":\"True\",\"cn_meeting\":\"False\",\"in_meeting\":\"False\",\"join_before_host\":\"False\",\"mute_upon_entry\":\"False\",\"watermark\":\"False\",\"use_pmi\":\"False\",\"approval_type\":\"0\",\"audio\":\"0\",\"auto_recording\":\"none\",\"enforce_login\":\"False\",\"registrants_email_notification\":\"False\"}}"
            envdict = dotenv_values('.env')

            print('EEEEE', payload)

            headers = {
                'content-type': "application/json",
                'authorization': envdict["TOKEN_URL"]
            }

            conn.request("POST", "/v2/users/justinjhes@gmail.com/meetings", payload, headers)
            data = json.load(conn.getresponse())

            # ZOOM JOIN URL
            print("THIS IS THE JOIN URL", data['join_url'])
            print("THIS IS THE JOIN URL", data['id'])
            print('TOKEN',load_dotenv('TOKEN_URL'))

            Languagetolearn(language_id=request.POST['language'], start_time_slot=request.POST['start_time_slot'],
                            end_time_slot=request.POST['end_time_slot'], child_id=id_,
                            date_slot=request.POST['date_slot'], meeting_id=data['id'], link_video=data['start_url']).save()
        #rqt = Languagetolearn.objects.filter(last_name_id=id_)

        return redirect(f"/mykids/{id_}/planning", {'form': EventForm})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['rqt'] = Languagetolearn.objects.filter(child_id=self.request.session['child_id'])

        # context['deleteEvent'] = delete_event(request, id_event=self.kwargs.get("id_event"))
        return context


"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print('CCCCC-----------', context)
        # print('SsSS-------------', self.request.GET.get('month', None))
        d1 = datetime.today()
        print('TTTTTToday---------------', d1)

        print('Year____TTTTTT', d1.year)
        print('Month____TTTTTTTT', d1.month)

        d = get_date(self.request.GET.get('month', None))

        # print('DDDDD---------------', d)
        # print('Year___DDDDDd', d.year)
        # print('Month___DDDDDDD', d.month)
        cal = Calendar(d.year, d.month)
        print('_______________________________________________')
        html_cal = cal.formatmonth(withyear=True)

        # print('_________', html_cal)
        context['calendar'] = mark_safe(html_cal)
        print('_______________________________________________')
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        return context

"""

"""

def event_details(request, event_id):
    event = Languagetolearn.objects.get(id=event_id)
    context = {
        'event': event,
    }
    return render(request, 'event-details.html', context)
"""



