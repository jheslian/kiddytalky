from django.urls import path, include

from .views import conversation_view, delete_message

app_name = 'conversation'

urlpatterns = [
    path('', conversation_view, name='messages'),
    path('<int:id_message>/delete_message', delete_message, name='delete_message')

]