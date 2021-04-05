from django.urls import path, include
from .views import home, conversation

app_name = "main"

urlpatterns = [
    path('', home, name="home"),
    path('messages/', conversation),
    path('correspondents/', include('correspondents.urls')),

]
