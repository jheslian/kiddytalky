from django.urls import path
from .views import previous_session_view

app_name = 'kiddytalks'

urlpatterns = [
    path('', previous_session_view, name='contacts')
]