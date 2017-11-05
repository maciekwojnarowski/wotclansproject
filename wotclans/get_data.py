from .models import Clan, Player
import requests

clan = Clan()
player = Player()


def get_clans_data():
    clans_json = 'https://api.worldoftanks.eu/wgn/clans/list/?application_id=58e1edcfb25f7033d5427a6918c5c7f1&page_no='

    page_no = 1
    while True:
        clans_data = requests.get(clans_json + str(page_no)).json()
        if clans_data['meta']['count'] > 0:
            for i in range(clans_data['meta']['count']):
                clan.full_name = clans_data['data'][i]['name']
                clan.members_count = clans_data['data'][i]['members_count']
                clan.color = clans_data['data'][i]['color']
                clan.created_at = clans_data['data'][i]['created_at']
                clan.tag = clans_data['data'][i]['tag']
                clan.clan_id = clans_data['data'][i]['clan_id']




