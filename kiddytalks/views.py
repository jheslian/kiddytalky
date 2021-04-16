from django.shortcuts import render
from django.views.generic import ListView
from main.models import Languagetolearn, Child, Parent, Language
# Create your views here.
from django.shortcuts import render
from crum import get_current_user
from django.db.models import Q

"""def previous_session_view(request):
    return render(request, 'previous_session.html')
"""


class PreviousSessionView(ListView):
    model = Languagetolearn
    template_name = 'previous_session.html'

    def get_context_data(self, **kwargs):
        context = super(PreviousSessionView, self).get_context_data(**kwargs)

        user_id = get_current_user().id
        #print('USER ID', user_id)
        parent = Parent.objects.get(user_id=user_id)

        # get a list of all kids belonging to the current parent except 1st child since its a dummy account
        parent_children = Child.objects.filter(parent_id=parent.id).exclude(id=1)

        #print("exclude", parent_children)

        # test = Languagetolearn.objects.all().values('child', 'child_correspondent')
        previous_sessions = []
        for child in parent_children:
            print("DEBUT BOUCLE FOR")
            # stores the foreign child id when my child is the host
            meetings_with_my_child_as_host = Languagetolearn.objects.filter(child_id=child.id).values('child_correspondent')
            print("HOOOOST",meetings_with_my_child_as_host[0]['child_correspondent'])

            """current_id = meetings_with_my_child_as_host[0]['child_correspondent']
            if current_id not in previous_sessions:
                # then add it to the final list
                previous_sessions.append(current_id)"""

            for kiddy_talk in meetings_with_my_child_as_host:
                current_id = kiddy_talk['child_correspondent']
                # checks if the current id to append is already known or not
                if current_id not in previous_sessions:
                    # then add it to the final list
                    previous_sessions.append(current_id)

            # stores the foreign child id when my child is the correspondent
            meetings_with_my_child_as_corr = Languagetolearn.objects.filter(child_correspondent_id=child.id).values('child')
            for kiddy_talk in meetings_with_my_child_as_corr:
                current_id = kiddy_talk['child']
                # check if the current id to append is already known
                #print("SSSSS,", meetings_with_my_child_as_corr)
                # current_id = meetings_with_my_child_as_corr[0]['child']
                if current_id not in previous_sessions:
                    # then add it to the final list
                    previous_sessions.append(current_id)

        print("EFESG PRZVIIOSFSQ", previous_sessions)

        # previous_sessions.append(Languagetolearn.objects.filter(child_correspondent_id=child.id))
        # exclure les id de nos propres enfants filtrage à faire sur la colone child_id ET child_correspondant
        print("Child SESSIONS", previous_sessions)
        # Optionnel, à voir: exclure les doublons d'enfants pour n'avoir qu'un exemplaire de chaque enfant avec qui on a eu des contacts
        """for l in previous_sessions:
            print(f"child: {l['child']} child correspondent: {l['child_correspondent']} ")"""

        return context

    """ context ={}
    for child in parent_children:
        print("DFGGFNF",child.id)

        context[child.id] = Languagetolearn.objects.filter(Q(child_id = child.id) | Q(child_correspondent_id=child.id))
        #print(context[child.id] )
    #print(Languagetolearn.objects.filter(child_correspondent_id__in=parent_children))

    print(parent_children)


    context['parent_childs'] = parent_children
    """

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
