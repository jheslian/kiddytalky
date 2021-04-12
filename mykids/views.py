from django.shortcuts import render
from main.models import Languagetolearn, Child, Language
from datetime import datetime, date
import datetime as dt
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta
import calendar

from django.urls import reverse_lazy
from django.views.generic import FormView

from main.models import *
from .utils import Calendar
from .forms import EventForm, AddMemberForm


def mykid_view(request):
    return render(request, 'mykids.html')


"""
def planning_view(request):
    if request.method == "POST":
        obj = Languagetolearn()
        obj.id_child = Child.objects.get(id=1)

        print('bonjour-----', obj.id_child)
        obj.id_language = Language.objects.get(name=request.POST["language"])
        print('bonjour-----', obj.id_language)
        obj.start_time_slot = request.POST["start_time_slot"]
        obj.end_time_slot = request.POST["end_time_slot"]
        obj.date_slot = request.POST["date"]
        obj.save()

    return render(request, 'planning.html')
"""


# cal/views.py


# AddMemberForm


# @login_required(login_url='signup')
def index(request):
    return HttpResponse('hello')


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


class planning_view(FormView, generic.ListView):
    # login_url = 'signup'
    model = Event
    form_class = EventForm
    template_name = 'planning.html'

    def post(self, request, *args, **kwargs):
        event_form = EventForm(request.POST)
        print('rrrrr', datetime.strptime(request.POST['date_slot'], "%Y-%m-%d") < datetime.today())
        if datetime.strptime(request.POST['date_slot'], "%Y-%m-%d") < datetime.today():
            messages.error(request, 'the date must be greater than today')
            return redirect('mykids:planning')

        elif request.POST['start_time'] >= request.POST['end_time']:
            messages.error(request, 'start date must be less than the end date ')
            return redirect('mykids:planning')
        elif event_form.is_valid():

            event_form.save()
            messages.success(request, 'the date slot is added')
            return redirect('mykids:planning')

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
        # print('_______________________________________________')
        html_cal = cal.formatmonth(withyear=True)

        # print('_________', html_cal)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        return context


""


class EventEdit(generic.UpdateView):
    model = Event
    fields = ['title', 'description', 'start_time', 'end_time']
    template_name = 'event.html'


# @login_required(login_url='signup')
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    eventmember = EventMember.objects.filter(event=event)
    context = {
        'event': event,
        'eventmember': eventmember
    }
    return render(request, 'event-details.html', context)


"""


def add_eventmember(request, event_id):
    forms = AddMemberForm()
    if request.method == 'POST':
        forms = AddMemberForm(request.POST)
        if forms.is_valid():
            member = EventMember.objects.filter(event=event_id)
            event = Event.objects.get(id=event_id)
            if member.count() <= 9:
                user = forms.cleaned_data['user']
                EventMember.objects.create(
                    event=event,
                    user=user
                )
                return redirect('calendarapp:calendar')
            else:
                print('--------------User limit exceed!-----------------')
    context = {
        'form': forms
    }
    return render(request, 'add_member.html', context)

"""


class EventMemberDeleteView(generic.DeleteView):
    model = EventMember
    template_name = 'event_delete.html'
    success_url = reverse_lazy('calendarapp:calendar')
