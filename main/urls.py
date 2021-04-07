from django.urls import path, include
from .views import *

app_name = "main"

urlpatterns = [
    path('', index_view),
    path('home', home, name="home"),
    path('account/', include('accounts.urls')),
    path('messages/', include('conversation.urls')),
    path('correspondents/', include('correspondents.urls')),
    path('myaccount/', include('myaccounts.urls')),
    path('mykids/', include('mykids.urls')),


]
