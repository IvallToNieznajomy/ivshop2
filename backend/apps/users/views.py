from rest_framework.views import APIView

from apps.users.oauth2.discord_oauth2 import DiscordOauth


class DiscordLogin(APIView):
    """
    Login using discord oauth2
    """
    def get(self, request, *args, **kwargs):
        return DiscordOauth.discord_login_url