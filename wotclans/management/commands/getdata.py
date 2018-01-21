import time
import datetime
from multiprocessing.dummy import Pool

import requests
from django.utils import timezone

from wotclans.models import Clan, Logo


# make the Pool of workers
pool = Pool(20)
pool.map()


def get_data(i):

    clan = Clan()
    logo = Logo()
    print(i['tag'])
    clan.full_name = i['name']
    clan.tag = i['tag']
    # clan.motto = clans_data['data'][i]['motto']
    clan.clan_id = i['clan_id']
    clan.members_count = i['members_count']
    clan.created_at = datetime.datetime.fromtimestamp(i['created_at'], timezone.utc)
    clan.color = i['color']
    # clan.description = clans_data['data'][i]['tag']
    # clan.description_html = clans_data['data'][i]['tag']
    clan.updated_at = timezone.now()

    clanratings_json = 'https://api.worldoftanks.eu/wot/clanratings/clans/?application_id=58e1edcfb25f7033d5427a6918c5c7f1&clan_id='
    clanratings_data = requests.get(clanratings_json + str(clan.clan_id)).json()
    try:
        clan.elo_gm_X = clanratings_data['data'][str(clan.clan_id)]['gm_elo_rating_10']['value']
    except:
        clan.elo_gm_X = 0
    try:
        clan.elo_gm_VIII = clanratings_data['data'][str(clan.clan_id)]['gm_elo_rating_8']['value']
    except:
        clan.elo_gm_VIII = 0
    try:
        clan.elo_sh_X = clanratings_data['data'][str(clan.clan_id)]['fb_elo_rating_10']['value']
    except:
        clan.elo_sh_X = 0
    try:
        clan.elo_sh_VIII = clanratings_data['data'][str(clan.clan_id)]['fb_elo_rating_8']['value']
    except:
        clan.elo_sh_VIII = 0
    try:
        clan.elo_sh_VI = clanratings_data['data'][str(clan.clan_id)]['fb_elo_rating_6']['value']
    except:
        clan.elo_sh_VI = 0
    clan.save()
    logo.clan_id = clan.clan_id
    logo.logo_big = i['emblems']['x195']['portal']
    logo.logo_small = i['emblems']['x32']['portal']
    logo.updated_at = timezone.now()
    logo.save()

    print(clan.tag + " added to DB")


clans_json = 'https://api.worldoftanks.eu/wgn/clans/list/?application_id=58e1edcfb25f7033d5427a6918c5c7f1&page_no='
# TODO: seems like this api call returns top clans first. maybe get only top 2000 clans?
for page_no in range(1, 20):
    start = time.time()
    clans_data = requests.get(clans_json + str(page_no)).json()
    if clans_data['meta']['count'] > 0:
        pool.map(get_data, clans_data['data'])
    else:
        break
    # print("site " + str(page_no) + " processed in " + str(time.time()-start))

pool.close()
pool.join()



