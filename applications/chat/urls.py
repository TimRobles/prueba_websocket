from django.urls import path
from . import views

app_name='chat_app'

urlpatterns = [
    path('', views.lobby, name='lobby'),
]