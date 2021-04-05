from django.urls import path
from .views import mykid_view

app_name = 'myaccounts'

urlpatterns = [
    path('', mykid_view)
]