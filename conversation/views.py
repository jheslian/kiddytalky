from django.shortcuts import render
from main.models import Parent, Message


def conversation_view(request):
    parent = Parent.objects.get(user_id=request.session['id_parent'])

    msgsent = Message.objects.filter(message_to=parent.id)
    msgreceived = Message.objects.filter(message_from=parent.id)

    print('id du parent est égale à ', request.session['id_parent'])
    print('id du parent est égale à ', parent.id)
    return render(request, 'msg.html', {'msgsent': msgsent, 'msgreceived': msgreceived})
