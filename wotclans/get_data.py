from wotclans.models import Clan, Player
import requests
from django.utils import timezone
import datetime


player = Player()


def get_clans_data():
    clans_json = 'https://api.worldoftanks.eu/wgn/clans/list/?application_id=58e1edcfb25f7033d5427a6918c5c7f1&page_no='

    page_no = 1
    while True:
        clans_data = requests.get(clans_json + str(page_no)).json()
        if clans_data['meta']['count'] > 0:
            for i in range(clans_data['meta']['count']):
                clan = Clan()
                clan.full_name = clans_data['data'][i]['name']
                clan.tag = clans_data['data'][i]['tag']
                # clan.motto = clans_data['data'][i]['motto']
                clan.clan_id = clans_data['data'][i]['clan_id']
                clan.members_count = clans_data['data'][i]['members_count']
                clan.created_at = datetime.datetime.fromtimestamp(clans_data['data'][i]['created_at'], timezone.utc)
                clan.color = clans_data['data'][i]['color']
                # clan.description = clans_data['data'][i]['tag']
                # clan.description_html = clans_data['data'][i]['tag']
                clan.updated_at = timezone.now()
                clanratings_json = 'https://api.worldoftanks.eu/wot/clanratings/clans/?application_id=58e1edcfb25f7033d5427a6918c5c7f1&clan_id='
                clanratings_data = requests.get(clanratings_json + str(clan.clan_id)).json()
                clan.elo_gm_X = clanratings_data['data'][str(clan.clan_id)]['gm_elo_rating_10']['value']
                clan.elo_gm_VIII = clanratings_data['data'][str(clan.clan_id)]['gm_elo_rating_8']['value']
                clan.elo_sh_X = clanratings_data['data'][str(clan.clan_id)]['fb_elo_rating_10']['value']
                clan.elo_sh_VIII = clanratings_data['data'][str(clan.clan_id)]['fb_elo_rating_8']['value']
                clan.elo_sh_VI = clanratings_data['data'][str(clan.clan_id)]['fb_elo_rating_6']['value']
                clan.save()
                print(clan.tag + " added to DB")

            page_no += 1
        else:
            break


get_clans_data()