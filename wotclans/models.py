# from django.contrib.postgres.fields import JSONField
from django.db import models


class Clan(models.Model):
    full_name = models.CharField(max_length=80)
    tag = models.CharField(max_length=5)
    motto = models.CharField(max_length=50, default='')
    clan_id = models.PositiveIntegerField()
    members_count = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(null=True)
    color = models.CharField(max_length=12, default='black')
    description = models.TextField(default='')
    description_html = models.TextField(default='')
    updated_at = models.DateTimeField(null=True)
    elo_gm_X = models.PositiveSmallIntegerField(null=True)
    elo_gm_VIII = models.PositiveSmallIntegerField(null=True)
    elo_sh_X = models.PositiveSmallIntegerField(null=True)
    elo_sh_VIII = models.PositiveSmallIntegerField(null=True)
    elo_sh_VI = models.PositiveSmallIntegerField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=25)
    account_id = models.PositiveIntegerField(null=True)
    last_updated = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=True)
    last_battle_time = models.DateTimeField(null=True)
    client_language = models.CharField(max_length=5)
    clan_id = models.ForeignKey(Clan)
    logout_at = models.DateTimeField(null=True)
    statistics_random = models.TextField(default='')
    statistics_gm10 = models.TextField(default='')
    statistics_gm8 = models.TextField(default='')
    statistics_gm6 = models.TextField(default='')
    statistics_skirmishes = models.TextField(default='')
    statistics_sh_defense = models.TextField(default='')



