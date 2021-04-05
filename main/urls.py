from django.urls import path, include
from .views import *

app_name = "main"

urlpatterns = [
    path('', home, name="home"),
    path('index', index_view),
    path('account/', include('accounts.urls')),
    path('messages/', include('conversation.urls')),
    path('correspondents/', include('correspondents.urls')),
    path('myaccount/', include('myaccounts.urls')),
    path('mykids/', include('mykids.urls')),


]
