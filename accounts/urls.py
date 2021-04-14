from django.urls import path
from .views import ParentRegisterView, login_request, logout_view, get_meeting

# app_name = 'accounts'

urlpatterns=[
     path('parent_register/', ParentRegisterView.as_view(), name='parent-register'),
     # path('child_register/',views.child_register.as_view(), name='child_register'),
     path('login/', login_request, name='login'),
     path('logout/', logout_view, name='logout'),
     #path('testapi/', get_meeting, name='get_meeting')
]
