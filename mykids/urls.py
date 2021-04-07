from django.urls import path
from .views import mykid_view, planning_view

app_name = 'mykids'

urlpatterns = [
    path('', mykid_view),
    path('planning/', planning_view),

]