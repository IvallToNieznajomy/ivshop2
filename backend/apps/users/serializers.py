from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):

    class Meta(object):
        model = User
        fields = ('username', 'account_type', 'avatar_url')