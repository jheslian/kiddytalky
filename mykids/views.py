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


class ChildListView(ListView):
    print("recover cacheZZPPPPPPPPPPPPPPPPPPPPPPPPPZZZ", cache.get('parent_id', 'has expired'))
    template_name = 'mykids.html'
    queryset = Child.objects.all().filter(parent_id=2)
    # queryset = Child.objects.all()


# print(request.session['id_parent'])

class MyChildView(DetailView):
    cache.get('id_parent')
    template_name = 'childview.html'

    def get_object(self):
        id_ = self.kwargs.get("id")

        print("PARENT ID MY KIDS:", cache.get('id_parent'))
        return get_object_or_404(Child, id=id_)


class UpdateChildView(UpdateView):
    form_class = EditChildInfo
    template_name = 'editprofile_enfant.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Child, id=id_)

    def get_success_url(self):
        return reverse('main:mykids:kids')


class DeleteChildView(DeleteView):
    model = Child
    template_name = 'delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Child, user_id=id_)

    def get_success_url(self):
        return redirect('main:mykids:kids')


class ChildRegisterView(CreateView):
    model = User
    form_class = ChildRegistrationForm
    template_name = 'child/child_register.html'

    def form_valid(self, form):
        form.save()
        return redirect('main:mykids:childregister')
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


# --------------------------------------------------------------------------

def mykid_view(request):
    return render(request, 'mykids.html')


# @login_required(login_url='signup')
def index(request):
    return HttpResponse('hello')


# ----------------------------
# -----------------------------
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
    model = Languagetolearn
    form_class = EventForm
    template_name = 'planning.html'

    def post(self, request, *args, **kwargs):
        print('PPPPPP', request.POST['start_time_slot'] >= request.POST['end_time_slot'])
        event_form = EventForm(request.POST)
        print('rrrrr', datetime.strptime(request.POST['date_slot'], "%Y-%m-%d") < datetime.today())
        if datetime.strptime(request.POST['date_slot'], "%Y-%m-%d") < datetime.today():
            messages.error(request, 'the date must be greater than today')
            return redirect("main:mykids:planning")

        elif request.POST['start_time_slot'] >= request.POST['end_time_slot']:
            messages.error(request, 'start date must be less than the end date ')
            return redirect("main:mykids:planning")
        elif event_form.is_valid():

            event_form.save()
            messages.success(request, 'the date slot is added')
            return redirect("main:mykids:planning")

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


def event_details(request, event_id):
    event = Languagetolearn.objects.get(id=event_id)
    #eventmember = EventMember.objects.filter(event=event)
    context = {
        'event': event,
       # 'eventmember': eventmember
    }
    return render(request, 'event-details.html', context)