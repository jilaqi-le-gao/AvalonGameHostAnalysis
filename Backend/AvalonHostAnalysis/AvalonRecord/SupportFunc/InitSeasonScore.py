from ..models import *
import datetime
from django.contrib.auth.models import User


def init_one_season(season_name: str, start: datetime.date, end: datetime.date):
    this_season = Seasons(SeasonName=season_name, SeasonStart=start, SeasonEnd=end)
    this_season.save()

    all_users = User.objects.all()

    for one_user in all_users:
        this_record = ScoreBoard(season=this_season, player=one_user, score=1000)
        this_record.save()

