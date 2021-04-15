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
from .formplanning import EventForm, SendMessage
from crum import get_current_user

"""class ChildListView(ListView):
template_name = 'mykids.html'

#e = get_current_user()
#print("HOME CRUMMMMMM", e.id)

def get_queryset(self, *args, **kwargs):
    id_ = self.kwargs.get("id")
    queryset = Child.objects.all().filter(parent_id=id_)
    return queryset"""

"""    def get(self, request, *args):
    request.GET.get('id')

    print("TTTTTTT", request.GET.get('id') )
    print("TTTTAAAATTT", self.request.session['id_parent'])

    return super(ChildListView, self).get(request, *args)"""


def child_list_view(request):
    print("inseide")
    user_id = request.session['id_parent']
    print("afteruser1", user_id)
    parent = Parent.objects.get(user_id=user_id)

    print("AAAAAA111111")

    queryset = Child.objects.filter(parent_id=parent.id)

    print('after queryyyyyyy:', queryset)
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
        return get_object_or_404(User, id=id_)


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
    # id_ = self.kwargs.get("id")
    id_ = request.session['child_id']
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

            Languagetolearn(language_id=request.POST['language'], start_time_slot=request.POST['start_time_slot'],
                            end_time_slot=request.POST['end_time_slot'], last_name_id=id_,
                            date_slot=request.POST['date_slot']).save()
        rqt = Languagetolearn.objects.filter(last_name_id=id_)

        return redirect(f"/mykids/{id_}/planning", {'form': EventForm})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['rqt'] = Languagetolearn.objects.filter(last_name_id=self.request.session['child_id'])

        # context['deleteEvent'] = delete_event(request, id_event=self.kwargs.get("id_event"))
        return context


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------


def sendmessage(request):
    form = SendMessage(request.POST)
    id_ = request.session['child_id']
    print('______________________',id_)
    if request.method == 'POST':

        print('XXXXXXXXX',request.POST['content'])

        Message(content=request.POST['content'], child_id=id_, message_from_id=1, message_to_id=1).save()

    return redirect(f"/mykids/{id_}/planning")
