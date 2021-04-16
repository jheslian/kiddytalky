from django.urls import path, include
from .views import *

app_name = "main"

urlpatterns = [
    # this is index view
    path('', index_view, name='index'),

    # MAIN MENU
    #path('home/', home_view, name='home'),
    path('home/', correspondent_list_view, name='home'),
    path('<int:id>', MeetingValidationView.as_view(), name='meeting-update'),
    path('accept/(?P<id_event>\d+)/(?P<id_child>\d+)', accept_event, name='accept-event'),
    path('contacts', include('kiddytalks.urls')),
    path('account/', include('accounts.urls')),
    path('messages/', include('conversation.urls')),
    path('myaccount/', include('myaccounts.urls')),
    path('mykids/', include('mykids.urls')),
]
