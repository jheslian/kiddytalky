from django.urls import path
from .views import my_account_view, UpdateParentView


app_name = 'myaccounts'

urlpatterns = [
    path('', my_account_view),
    path('<int:id>/edit/', UpdateParentView.as_view(), name='edit-parent')
]