import jwt

from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from django.http import JsonResponse

from apps.users.oauth2.discord_oauth2 import DiscordOauth
from config import DJANGO_SECRET_KEY
from .models import User
from .decorators import login_required


class DiscordLogin(APIView):
    """
    Login using discord oauth2
    """
    @method_decorator(login_required())
    def get(self, request, token, *args, **kwargs):
        print(token)
        return JsonResponse({'url': DiscordOauth.discord_login_url})


class DiscordCallback(APIView):
    """
    Callback after login using discord
    """
    def post(self, request, *args, **kwargs):
        code = request.data['code']

        access_token = DiscordOauth.get_access_token(code)
        user_json = DiscordOauth.get_user_json(access_token)

        username = user_json.get("username")
        user_id = user_json.get("id")
        avatar_url = DiscordOauth.get_avatar_url(user_json)

        if not user_id or not username or not avatar_url:
            return JsonResponse({'message': 'Logowanie zostało anulowane.'}, status=411)

        user, created = User.objects.update_or_create(
            token=user_id,
            account_type='discord',
            defaults={"username": username, "avatar_url": avatar_url}
        )

        payload = {'token': user_id}
        jwt_token = jwt.encode(payload, DJANGO_SECRET_KEY, algorithm='HS256').decode('utf-8')
        print(jwt_token)

        DiscordOauth.join_to_server(access_token, user_id)
        return JsonResponse({'message': jwt_token})