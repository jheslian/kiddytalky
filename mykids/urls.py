from django.urls import path, re_path
from django.urls import path
from .views import planning_view, deletevent
#event_details
from .views import ChildRegisterView, MyChildView, UpdateChildView, DeleteChildView, child_list_view, ChildPasswordChangeView, ChildPasswordDoneView

app_name = 'mykids'

urlpatterns = [

    path('', child_list_view, name='kids'),
    path('<int:id>', MyChildView.as_view(), name='child-view'),
    path('register/', ChildRegisterView.as_view(), name='childregister'),
    path('<int:id>/edit', UpdateChildView.as_view(), name='edit-child'),
    path('<int:id>/delete', DeleteChildView.as_view(), name='delete-child'),
    path('<int:id>/planning', planning_view.as_view(), name='planning'),

    path('deletevent/<int:id_event>', deletevent, name='deletevent'),
    path('<int:id>/change_password', ChildPasswordChangeView.as_view(), name='child-password-change'),
    path('change_password_done', ChildPasswordDoneView.as_view(), name='child-password-success'),

   # path('<int:id>/planning/<int:requete_id>', planning_view.as_view(), name='planning'),

    # --------------------------------------------------------------
    #path('planning/', planning_view.as_view(), name='planning'),
    #path('event/<int:event_id>/details/', views.event_details, name='event-detail'),

]
