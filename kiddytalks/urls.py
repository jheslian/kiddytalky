from django.urls import path
from .views import PreviousSessionView, session

app_name = 'kiddytalks'

urlpatterns = [
    #path('', PreviousSessionView.as_view(), name='contacts'),
    path('', session, name='contacts'),

]