import jwt

from django.http import JsonResponse
from django.conf import settings

def login_required():
    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if 'Authorization' not in request.headers:
                return JsonResponse({'message': 'Login required.'}, status=401)

            jwt_token = request.headers['Authorization']
            try:
                jwt_data = jwt.decode(jwt_token, settings.SECRET_KEY, verify=True)
                token = jwt_data['token']
            except Exception as e:
                return JsonResponse({'message': 'Wrong jwt token.'}, status=401)
            return function(request, token, *args, **kwargs)
        return wrapper
    return decorator