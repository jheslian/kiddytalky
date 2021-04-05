from django.urls import path
from .views import correspondent_view

# app_name = 'correspondents'

urlpatterns = [
    path('', correspondent_view)
]