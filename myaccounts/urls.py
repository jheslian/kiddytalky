from django.urls import path
from .views import my_account_view

app_name = 'myaccounts'

urlpatterns = [
    path('', my_account_view)
]