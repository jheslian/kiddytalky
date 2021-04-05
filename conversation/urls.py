from django.urls import path, include

from .views import conversation

app_name = conversation

urlpatterns = [
    path('', conversation),
    
]