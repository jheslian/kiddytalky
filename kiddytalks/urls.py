from django.urls import path
from .views import PreviousSessionView

app_name = 'kiddytalks'

urlpatterns = [
    path('', PreviousSessionView.as_view(), name='contacts')
    ]