from django.shortcuts import render
from django.views.generic import View
from wotclans.models import Clan, Logo


class HomeView(View):
    def get(self, request):
        clans2 = Clan.objects.raw('''SELECT *
                                    FROM wotclans_clan a
                                    INNER JOIN (
                                        SELECT clan_id, max(updated_at) maxupdated
                                        FROM wotclans_clan
                                        GROUP BY clan_id
                                        ) b ON a.clan_id = b.clan_id AND a.updated_at = b.maxupdated
                                        ORDER BY "elo_gm_X" DESC ''')
        clans = Clan.objects.raw('''SELECT *
                                     FROM (
                                        SELECT *
                                        FROM wotclans_clan a
                                        INNER JOIN (
                                          SELECT clan_id, max(updated_at) maxupdated
                                          FROM wotclans_clan
                                          GROUP BY clan_id
                                          ) b ON a.clan_id = b.clan_id AND a.updated_at = b.maxupdated) w
                                      INNER JOIN wotclans_logo l 
                                      ON w.tag = l.tag
                                      ORDER BY "elo_gm_X" DESC''')
        # logos = Logo()
        # for clan in clans:
        #     logos = logos + Logo.objects.filter(tag=clan.tag)

        return render(request, 'home.html', {'clans': clans, })
