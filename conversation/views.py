from django.shortcuts import render, reverse
from main.models import Parent, Message
from django.db import connection
from collections import namedtuple
from django.shortcuts import redirect


def dictfetchall(cursor):
    # Return all rows from a cursor as a dict
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def conversation_view(request):
    parent = Parent.objects.get(user_id=request.session['id_parent'])
    request.session['id_parent_parent'] = parent.id
    print('id_parent_parent', parent.id)

    # msgreceived = Message.objects.filter(message_to=parent.id)
    # msgsent = Message.objects.filter(message_from=parent.id)

    # ------------------------- receive messages --------------- :
    with connection.cursor() as c:
        c.execute(
            "SELECT main_message.id,main_message.child_id,main_message.message_from_id, main_message.message_date, main_parent.email,main_child.first_name,"
            " main_message.content, main_parent.first_name as parent_name FROM main_message, main_child, main_parent  "
            "WHERE main_child.id = main_message.child_id AND "
            "main_message.message_from_id = main_parent.id AND"
            " main_message.message_to_id = %s", [parent.id])

        # msgreceived = c.fetchall()
        msgreceived = dictfetchall(c)
        # for test in msgreceived:

        # print(test)

    # ----------------- sent messages---------- :

    with connection.cursor() as c:
        c.execute("SELECT main_message.id, main_message.message_date, main_parent.email,main_child.first_name,"
                  " main_message.content, main_parent.first_name as parent_name FROM main_message, main_child, main_parent  "
                  "WHERE main_child.id = main_message.child_id AND "
                  "main_message.message_from_id = main_parent.id AND"
                  " main_message.message_from_id = %s", [parent.id])

        # msgreceived = c.fetchall()
        msgsent = dictfetchall(c)

    # print('id du parent est égale à ', request.session['id_parent'])

    # print('id du parent est égale à ', parent.id)
    # print('msg reçu', msgsent)
    # print('msg reçu', msgreceived)
    return render(request, 'msg.html', {'msgsent': msgsent, 'msgreceived': msgreceived})


# ----------------------------------- Delete message------------------------------------------------------

def delete_message(request, id_message):
    print(id_message)
    Message.objects.get(id=id_message).delete()

    return redirect("main:conversation:messages")


# ------------------------------------ send a message  form----------------------------------------------------

def send_msg(request, id):
    context = {}
    # context['message_from_id'] = message_from_id
    # context['child_id']= child_id
    context['id'] = id

    #print('testtttttt', id)

    return render(request, 'sendmessage.html', context)


# --------------------------------------------------------------------------------------------------------


# ------------------------------------ answer message ----------------------------------------------------
# ----------! attention à modifier peut-ête

def answer_message(request, id):
    # id_ = request.session['child_id']
    message = Message.objects.get(id=id)
    id_from = message.message_from_id
    id_ = message.child_id
    print('______________________child  form', id_, id_from )

    if request.method == 'POST':
        Message(content=request.POST['content'], child_id=id_, message_from_id=request.session['id_parent_parent'],
                message_to_id=id_from).save()

    return redirect('main:conversation:messages')
# --------------------------------------------------------------------------------------------------------
