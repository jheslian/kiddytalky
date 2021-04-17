from django.urls import path
from .views import child_home_view, child_activity_view,child_profile_view, child_history_view, friend_profile_view

app_name = "child_account"

urlpatterns = [
    path('', child_home_view, name='child-home'),
    path('activity', child_activity_view, name='child-activity'),
    path('history', child_history_view, name='child-history'),
    path('profile', child_profile_view, name='child-profile'),
    path('friend-profile/(?P<id>\d+)', friend_profile_view, name='friend-profile'),

]