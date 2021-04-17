from django.shortcuts import render, redirect
from django.contrib.auth import logout
from main.models import Languagetolearn, Child, Language
from datetime import datetime
from django.db import connection


# Create your views here.
def child_home_view(request):
    return render(request, 'child_home.html')


def child_activity_view(request):
    context = get_context_data(request, "activity")
    return render(request, 'child_activity.html', context)


def child_history_view(request):
    context = get_context_data(request, "history")
    return render(request, 'child_history.html', context)


def child_profile_view(request):
    user_id_child = request.session['id_child_app']
    child = Child.objects.get(user_id=user_id_child)
    profile = Child.objects.get(id=child.id)
    context = {
        'profile': profile
    }

    return render(request, 'child_profile.html', context)


def friend_profile_view(request, id):

    profile = Child.objects.get(id=id)
    context = {
        'profile': profile
    }

    return render(request, 'child_profile.html', context)


def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('/')


def get_context_data(request, menu_type):
    context = {}

    user_id_child = request.session['id_child_app']
    child = Child.objects.get(user_id=user_id_child)

    future_session = []
    meetings_where_i_host = []
    meetings_as_corr = []
    sessions_id = []
    if menu_type == "history":
        meetings_where_i_host = Languagetolearn.objects.filter(child_id=child.id). \
            values('child_correspondent', 'start_time_slot', 'end_time_slot', 'date_slot', 'link_video', 'language'). \
            filter(date_slot__lte=datetime.today()).filter(end_time_slot__lte=datetime.today().now())
    elif menu_type == "activity":
        meetings_where_i_host = Languagetolearn.objects.filter(child_id=child.id). \
            values('child_correspondent', 'start_time_slot', 'end_time_slot', 'date_slot', 'link_video', 'language'). \
            filter(date_slot__gte=datetime.today()).filter(end_time_slot__gte=datetime.today().now())
    for kiddy_talk in meetings_where_i_host:
        current_id = kiddy_talk['child_correspondent']
        start_time = kiddy_talk['start_time_slot']
        end_time = kiddy_talk['end_time_slot']
        date = kiddy_talk['date_slot']
        language = kiddy_talk['language']
        link = kiddy_talk['link_video']
        sessions_id.append(current_id)

        meeting = {'id': current_id, 'start_time': start_time, 'end_time': end_time, 'date': date, 'language': language, 'link': link}
        future_session.append(meeting)

        # stores the foreign child id when my child is the correspondent
    if menu_type == "history":
        meetings_as_corr = Languagetolearn.objects.filter(child_correspondent_id=child.id) \
            .values('child', 'start_time_slot', 'end_time_slot', 'date_slot', 'link_video', 'language').filter(date_slot__lte=datetime.today()).filter(
            end_time_slot__lte=datetime.today().now())
    elif menu_type == "activity":
        meetings_as_corr = Languagetolearn.objects.filter(child_correspondent_id=child.id) \
            .values('child', 'start_time_slot', 'end_time_slot', 'date_slot', 'link_video', 'language').filter(date_slot__gte=datetime.today()).filter(
            end_time_slot__gte=datetime.today().now())
    print("TIME", meetings_as_corr)
    for kiddy_talk in meetings_as_corr:
        current_id = kiddy_talk['child']
        start_time = kiddy_talk['start_time_slot']
        end_time = kiddy_talk['end_time_slot']
        date = kiddy_talk['date_slot']
        language = kiddy_talk['language']
        link = kiddy_talk['link_video']
        sessions_id.append(current_id)

        meeting = {'id': current_id, 'start_time': start_time, 'end_time': end_time,  'language': language, 'date': date, 'link': link}

        future_session.append(meeting)

    context['meetings'] = future_session

    # recover child data
    children_to_display = []
    for index, child_id in enumerate(sessions_id):
        children_to_display.append(Child.objects.filter(id=child_id))
        print("XXX", children_to_display)

    context['children'] = Child.objects.all()
    context['languages'] = Language.objects.all()
    print(context['languages'])


    return context