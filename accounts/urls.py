from django.urls import path, include

from .views import *


app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register_parent, name="register"),
    path('logout', logout_view, name="logout")
]
