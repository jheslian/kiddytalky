from django.urls import path
from .views import update_parent_view, DeleteParentView, MyAccountView, ParentPasswordDoneView, ParentPasswordChangeView


app_name = 'myaccounts'

urlpatterns = [
    path('<int:id>', MyAccountView.as_view(), name='my-account'),
    #path('<int:id>', my_account_view, name='my-account'),
    path('<int:id>/edit/', update_parent_view, name='edit-parent'),
    path('<int:id>/delete', DeleteParentView.as_view(), name='delete-parent'),
    path('<int:id>/change_password', ParentPasswordChangeView.as_view(), name='parent-password-change'),
    path('change_password_done', ParentPasswordDoneView.as_view(), name='parent-password-succes'),

]