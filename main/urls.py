from django.urls import path, include
from .views import *

app_name = "main"

urlpatterns = [
    path('', index_view, name='index'),
    path('home/', home_view, name='home'),
    path('contacts', include('kiddytalks.urls')),
    path('account/', include('accounts.urls')),
    path('messages/', include('conversation.urls')),
    path('myaccount/', include('myaccounts.urls')),
    path('mykids/', include('mykids.urls')),


]
