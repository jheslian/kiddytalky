from django.urls import path

from accounts.views import (RegisterParentView, ParentDetailView)

app_name = 'accounts'
urlpatterns = [
    path('register/', RegisterParentView.as_view(), name="register-parent"),
    path('<int:id>', ParentDetailView.as_view(), name="parent-detail"),
]
