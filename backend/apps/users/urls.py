from . import views

from django.urls import path

urlpatterns = [
    path('me/', views.UserData.as_view()),
    path('login/discord/', views.DiscordLogin.as_view()),
    path('login/discord/callback/', views.DiscordCallback.as_view())
]
