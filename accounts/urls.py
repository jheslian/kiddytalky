from django.urls import path

from .views import *


app_name = 'accounts'
urlpatterns = [
    path('login', login_view, name="login"),
    path('register/', RegisterParentView.as_view(), name="register"),
    path('logout', logout_view, name="logout")

    # path('<int:id>', ParentDetailView.as_view(), name="parent-detail"),
]
