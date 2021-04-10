from django.urls import path, re_path
from .views import mykid_view,  ChildRegisterView,MyChildView #UpdateChildView, DeleteChildView

app_name = 'mykids'

urlpatterns = [
    path('', mykid_view, name='kids'),
    path('register/', ChildRegisterView.as_view(), name='childregister'),
    # path('', mykid_view, name='kids'),
    # path('<int:id>/edit', UpdateChildView.as_view(), name='edit-parent'),
    # path('<int:id>/delete', DeleteChildView.as_view(), name='delete-parent'),

]