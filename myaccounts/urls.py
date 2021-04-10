from django.urls import path
from .views import my_account_view, UpdateParentView, DeleteParentView, MyAccountView


app_name = 'myaccounts'

urlpatterns = [
    path('<int:id>', MyAccountView.as_view(), name='my-account'),
    path('<int:id>/edit', UpdateParentView.as_view(), name='edit-parent'),
    path('<int:id>/delete', DeleteParentView.as_view(), name='delete-parent')
]