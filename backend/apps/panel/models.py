from django.db import models

from apps.users.models import User


class Shop(models.Model):
    name = models.CharField(max_length=32)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    general_settings = models.CharField(max_length=2048, blank=True)  # json array
    customization_settings = models.CharField(max_length=2048, blank=True)  # json array
    widget_settings = models.CharField(max_length=2048, blank=True)  # json array


class Server(models.Model):
    name = models.CharField(max_length=32)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    ip = models.CharField(max_length=253)  # ip address or domain of server
    rcon_port = models.IntegerField()
    rcon_password = models.CharField(max_length=128)
    admins = models.ManyToManyField(User)
