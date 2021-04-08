from django.urls import path
from . import views

urlpatterns=[
     #path('register/',views.register, name='register'),
     path('parent_register/',views.parent_register.as_view(), name='parent_register'),
     path('child_register/',views.child_register.as_view(), name='child_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]


"""from django.urls import path, include

from .views import *


app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register_parent, name="register"),
    path('logout', logout_view, name="logout")
]
"""