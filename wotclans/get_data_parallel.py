# python manage.py shell < wotclans/get_data_parallel.py

import time
from datetime import datetime, timedelta
from multiprocessing.dummy import Pool
import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.utils import timezone
from wotclans.models import Clan, Logo


# make the Pool of workers
pool = Pool(20)
print('Pool map created')


def get_data(i):
    clan = Clan()
    logo = Logo()
    print(i['tag'])
    clan.full_name = i['name']
    clan.tag = i['tag']
    # clan.motto = clans_data['data'][i]['motto']
    clan.clan_id = i['clan_id']
    clan.members_count = i['members_count']
    clan.created_at = datetime.fromtimestamp(i['created_at'], timezone.utc)
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
    """
    this is stupid and should be done by function, but idc
    """
    if Logo.objects.filter(tag=clan.tag) and datetime.now(timezone.utc) - Logo.objects.filter(tag=clan.tag).first().updated_at > timedelta(days=3):
        Logo.objects.filter(tag=clan.tag).delete()  # django_cleanup deletes the files
        logo.clan_id = clan  # clan.id
        logo.tag = clan.tag
        imgb = requests.get(i['emblems']['x195']['portal'])
        imgs = requests.get(i['emblems']['x32']['portal'])
        tempb = NamedTemporaryFile()
        temps = NamedTemporaryFile()
        tempb.write(imgb.content)
        temps.write(imgs.content)
        tempb.flush()
        temps.flush()
        logo.logo_big.save("{}{}".format(clan.tag, ".png"), File(tempb), save=True)
        logo.logo_small.save("{}{}".format(clan.tag, ".png"), File(temps), save=True)
        logo.updated_at = timezone.now()
        logo.save()
    elif not Logo.objects.filter(tag=clan.tag):
        logo.clan_id = clan  # clan.id
        logo.tag = clan.tag
        imgb = requests.get(i['emblems']['x195']['portal'])
        imgs = requests.get(i['emblems']['x32']['portal'])
        tempb = NamedTemporaryFile()
        temps = NamedTemporaryFile()
        tempb.write(imgb.content)
        temps.write(imgs.content)
        tempb.flush()
        temps.flush()
        logo.logo_big.save("{}{}".format(clan.tag, ".png"), File(tempb), save=True)
        logo.logo_small.save("{}{}".format(clan.tag, ".png"), File(temps), save=True)
        logo.updated_at = timezone.now()
        logo.save()
    print(clan.tag + " added to DB")


clans_json = 'https://api.worldoftanks.eu/wgn/clans/list/?application_id=58e1edcfb25f7033d5427a6918c5c7f1&page_no='
# TODO: seems like this api call returns top clans first. maybe get only top 2000 clans?
print('Starting main loop')
start = time.time()
for page_no in range(1, 10):  # TODO: change it back to 1,20
    print("{} {}".format("Loop iteration number", page_no))
    clans_data = requests.get(clans_json + str(page_no)).json()
    if clans_data['status'] == 'ok' and clans_data['meta']['count'] > 0:
        pool.map(get_data, clans_data['data'])
    else:
        break

print("Processed in " + str(time.time()-start) + " seconds")
pool.close()
pool.join()
