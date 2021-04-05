from django.urls import path

from .views import (RegisterParentView, ParentDetailView, login_view)


app_name = 'accounts'
urlpatterns = [
    path('login', login_view),
    path('register/', RegisterParentView.as_view(), name="register-parent"),
    path('<int:id>', ParentDetailView.as_view(), name="parent-detail"),
]
