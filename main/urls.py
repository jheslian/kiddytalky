from django.urls import path, include
from .views import *

app_name = "main"

urlpatterns = [
    # this is index view
    path('', index_view, name='index'),


    # ZOOM MEETING OK
    #path('', create_meeting),

    #path('', get_meeting),

    # NOT OK
    #path('', update_meeting),






    # MAIN MENU
    #path('home/', home_view, name='home'),
    path('home/', CorrespondentListView.as_view(), name='home'),
    #path('<int:id>', CorrespondentDetailView.as_view(), name="correspondent-detail"),
    path('<int:id>', MeetingValidationView.as_view(), name='meeting-update'),







    path('contacts', include('kiddytalks.urls')),
    path('account/', include('accounts.urls')),
    path('messages/', include('conversation.urls')),
    path('myaccount/', include('myaccounts.urls')),
    path('mykids/', include('mykids.urls')),

]
