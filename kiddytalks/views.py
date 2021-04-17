from django.shortcuts import render
from django.views.generic import ListView
from main.models import Languagetolearn, Child, Parent, Language
from .forms import SelectForm
from crum import get_current_user
from _datetime import datetime

"""def previous_session_view(request):
    return render(request, 'previous_session.html')
"""


def session(request):
    context = {}
    user_id = get_current_user().id
    # print('USER ID', user_id)
    parent = Parent.objects.get(user_id=user_id)

    # option for select to choose which child correspondent should appear
    option = Child.objects.filter(parent_id=parent.id)
    context['select_child'] = option

    my_child = request.GET.get('option')
    print("LLLLLL", my_child)

    # get a list of all kids belonging to the current parent except 1st child since its a dummy account
    if my_child:
        parent_children = Child.objects.filter(id=my_child)
    else:
        parent_children = Child.objects.filter(parent_id=parent.id).exclude(id=1)

    # print("exclude", parent_children)

    # test = Languagetolearn.objects.all().values('child', 'child_correspondent')
    previous_sessions = []
    for child in parent_children:
        # stores the foreign child id when my child is the host
        meetings_with_my_child_as_host = Languagetolearn.objects.filter(child_id=child.id). \
            values(
            'child_correspondent')  # .filter(date_slot__lte=datetime.today()).filter(end_time_slot__lte=datetime.now())

        for kiddy_talk in meetings_with_my_child_as_host:
            current_id = kiddy_talk['child_correspondent']
            # checks if the current id to append is already known or not
            if current_id not in previous_sessions:
                # then add it to the final list
                previous_sessions.append(current_id)

        # stores the foreign child id when my child is the correspondent
        meetings_with_my_child_as_corr = Languagetolearn.objects.filter(child_correspondent_id=child.id) \
            .values('child')  # .filter(date_slot__lte=datetime.today()).filter(end_time_slot__lte=datetime.now())
        print("TIME", meetings_with_my_child_as_corr)
        for kiddy_talk in meetings_with_my_child_as_corr:
            current_id = kiddy_talk['child']
            # check if the current id to append is already known
            if current_id not in previous_sessions:
                # then add it to the final list
                previous_sessions.append(current_id)

    print("TO DISPLAY: ", previous_sessions)

    children_to_display = []
    for index, child_id in enumerate(previous_sessions):
        children_to_display.append(Child.objects.filter(id=child_id))

    context["content"] = children_to_display
    print('CONTEXT DATA', context["content"])

    return render(request, 'previous_session.html', context)


class PreviousSessionView(ListView):
    model = Languagetolearn
    template_name = 'previous_session.html'

    def get_context_data(self, **kwargs):
        context = super(PreviousSessionView, self).get_context_data(**kwargs)

        user_id = get_current_user().id
        # print('USER ID', user_id)
        parent = Parent.objects.get(user_id=user_id)

        # option for select to choose which child correspondent should appear
        option = Child.objects.filter(parent_id=parent.id)
        context['select_child'] = option

        # get a list of all kids belonging to the current parent except 1st child since its a dummy account
        parent_children = Child.objects.filter(parent_id=parent.id).exclude(id=1)

        # test = Languagetolearn.objects.all().values('child', 'child_correspondent')
        previous_sessions = []
        for child in parent_children:
            # stores the foreign child id when my child is the host
            meetings_with_my_child_as_host = Languagetolearn.objects.filter(child_id=child.id). \
                values(
                'child_correspondent')  # .filter(date_slot__lte=datetime.today()).filter(end_time_slot__lte=datetime.now())

            for kiddy_talk in meetings_with_my_child_as_host:
                current_id = kiddy_talk['child_correspondent']
                # checks if the current id to append is already known or not
                if current_id not in previous_sessions:
                    # then add it to the final list
                    previous_sessions.append(current_id)

            # stores the foreign child id when my child is the correspondent
            meetings_with_my_child_as_corr = Languagetolearn.objects.filter(child_correspondent_id=child.id) \
                .values('child')  # .filter(date_slot__lte=datetime.today()).filter(end_time_slot__lte=datetime.now())
            print("TIME", meetings_with_my_child_as_corr)
            for kiddy_talk in meetings_with_my_child_as_corr:
                current_id = kiddy_talk['child']
                # check if the current id to append is already known to avoid duplicates
                if current_id not in previous_sessions:
                    # then add it to the final list
                    previous_sessions.append(current_id)

        print("Child SESSIONS", previous_sessions)
        children_to_display = []
        # Stores the children list into a list and pass it to the template using a context
        for index, child_id in enumerate(previous_sessions):
            children_to_display.append(Child.objects.filter(id=child_id))

        context["content"] = children_to_display
        print('CONTEXT DATA', context["content"])

        return context

    # get all meetings from languagetolearn that contains the ids belonging to the current parent.
    # past_meetings = []
    # past_meetings.append(Languagetolearn.objects.filter(child_id=''))
    # print(Languagetolearn.objects.filter(child_correspondent_id__in=parent_children.values_list('id', flat=True)))

    # Then, only keep the meetings whose timestamp is smaller than the current timestamp

    # context['proposition'] = Languagetolearn.objects.filter(child_id=id_, validation_status='Pending')

    # option for the select which contains the kids who will accept the proposition

    # option = Child.objects.filter(parent_id=parent.id)
    # context['select_child'] = option


# this are the details the child
"""        child = Child.objects.filter(id=id_)
context['child_data'] = child"""
