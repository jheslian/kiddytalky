from django.urls import path, re_path
from .views import ChildRegisterView, ChildListView, MyChildView, UpdateChildView, DeleteChildView

app_name = 'mykids'

urlpatterns = [
    path('', ChildListView.as_view(), name='kids'),
    path('<int:id>', MyChildView.as_view(), name='child-view'),
    path('register/', ChildRegisterView.as_view(), name='childregister'),
    path('<int:id>/edit', UpdateChildView.as_view(), name='edit-child'),
    path('<int:id>/delete', DeleteChildView.as_view(), name='delete-child'),

]