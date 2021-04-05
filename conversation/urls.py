from django.urls import path, include

from .views import conversation_view

app_name = 'conversation'

urlpatterns = [
    path('', conversation_view),
    
]