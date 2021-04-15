from django.urls import path, re_path
from django.urls import path, include
from .views import planning_view, deletevent, sendmessage
# event_details
from .views import ChildRegisterView, MyChildView, UpdateChildView, DeleteChildView, child_list_view

app_name = 'mykids'

urlpatterns = [

    path('', child_list_view, name='kids'),
    path('<int:id>', MyChildView.as_view(), name='child-view'),
    path('register/', ChildRegisterView.as_view(), name='childregister'),
    path('<int:id>/edit', UpdateChildView.as_view(), name='edit-child'),
    path('<int:id>/delete', DeleteChildView.as_view(), name='delete-child'),
    path('<int:id>/planning', planning_view.as_view(), name='planning'),
    path('deletevent/<int:id_event>', deletevent, name='deletevent'),
    path('sendmessage', sendmessage, name='sendmessage'),

    # path('messages/', include('conversation.urls')),

    # path('<int:id>/planning/<int:requete_id>', planning_view.as_view(), name='planning'),

    # --------------------------------------------------------------
    # path('planning/', planning_view.as_view(), name='planning'),
    # path('event/<int:event_id>/details/', views.event_details, name='event-detail'),

]
