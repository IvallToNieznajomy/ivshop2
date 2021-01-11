from rest_framework import serializers

from .models import Shop


class ShopSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Shop
        fields = ('id', 'name', 'owner', 'general_settings', 'customization_settings', 'widget_settings')