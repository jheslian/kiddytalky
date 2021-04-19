from django.urls import path, include

from .views import conversation_view, delete_message,send_msg, answer_message

app_name = 'conversation'

urlpatterns = [
    path('', conversation_view, name='messages'),
    path('<int:id_message>/delete_message', delete_message, name='delete_message'),
    path('<int:id>/send_msg', send_msg, name='send_msg'),
    path('<int:id>/answer_message', answer_message,name='answer_message')
]
