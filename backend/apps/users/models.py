from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64)
    token = models.CharField(max_length=255)
    account_type = models.CharField(max_length=16)  # discord or google
    avatar_url = models.URLField(blank=True)