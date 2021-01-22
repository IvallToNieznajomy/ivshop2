from rest_framework import serializers

from .models import Shop, Server


class ShopSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Shop
        fields = ('id', 'name', 'owner', 'general_settings', 'customization_settings', 'widget_settings')


class ServerSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Server
        fields = ('id', 'name', 'shop', 'ip', 'rcon_port', 'admins')