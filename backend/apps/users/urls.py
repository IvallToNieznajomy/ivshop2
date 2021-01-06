from . import views

from django.urls import path

urlpatterns = [
    path('login/discord', views.DiscordLogin.as_view())
]
