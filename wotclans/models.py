# from django.contrib.postgres.fields import JSONField
from django.db import models


class Clan(models.Model):
    full_name = models.CharField(max_length=50)
    tag = models.CharField(max_length=5)
    motto = models.CharField(max_length=50, null=True)
    clan_id = models.PositiveIntegerField()
    members_count = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(null=True)
    color = models.CharField(max_length=12, default='black')
    description = models.TextField(null=True)
    description_html = models.TextField(null=True)
    updated_at = models.DateTimeField(null=True)
    elo_gm_X = models.PositiveSmallIntegerField(null=True)
    elo_gm_VIII = models.PositiveSmallIntegerField(null=True)
    elo_sh_X = models.PositiveSmallIntegerField(null=True)
    elo_sh_VIII = models.PositiveSmallIntegerField(null=True)
    elo_sh_VI = models.PositiveSmallIntegerField(null=True)


class Player(models.Model):
    name = models.CharField(max_length=25)
    account_id = models.PositiveIntegerField()
    last_updated = models.DateTimeField()
    created_at = models.DateTimeField(null=True)
    last_battle_time = models.DateTimeField(null=True)
    client_language = models.CharField(max_length=5)
    clan_id = models.ForeignKey(Clan)
    logout_at = models.DateTimeField(null=True)
    statistics_random = models.TextField(null=True)
    statistics_gm10 = models.TextField(null=True)
    statistics_gm8 = models.TextField(null=True)
    statistics_gm6 = models.TextField(null=True)


