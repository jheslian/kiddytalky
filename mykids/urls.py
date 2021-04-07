from django.urls import path
from .views import mykid_view

app_name = 'mykids'

urlpatterns = [
    path('', mykid_view)
]