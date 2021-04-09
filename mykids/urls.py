from django.urls import path
from .views import mykid_view,  ChildRegisterView #, UpdateChildView, DeleteChildView,

app_name = 'mykids'

urlpatterns = [
    #path('', MyChildView.as_view(), name='kids'),
    path('', mykid_view, name='kids'),
    # path('<int:id>/edit', UpdateChildView.as_view(), name='edit-parent'),
    # path('<int:id>/delete', DeleteChildView.as_view(), name='delete-parent'),
    path('child_register/', ChildRegisterView.as_view(), name='child-register'),
]