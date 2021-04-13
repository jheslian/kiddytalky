from django.urls import path, re_path
from django.urls import path
from .views import mykid_view, planning_view
from .views import ChildRegisterView, MyChildView, UpdateChildView, DeleteChildView, child_list_view

app_name = 'mykids'

urlpatterns = [

    #path('<int:id>', ChildListView.as_view(), name='kids'),
    path('', child_list_view, name='kids'),
    path('<int:id>', MyChildView.as_view(), name='child-view'),
    path('register/', ChildRegisterView.as_view(), name='childregister'),
    path('<int:id>/edit', UpdateChildView.as_view(), name='edit-child'),
    path('<int:id>/delete', DeleteChildView.as_view(), name='delete-child'),
    path('', mykid_view),
    path('planning/', planning_view.as_view(), name='planning'),

]