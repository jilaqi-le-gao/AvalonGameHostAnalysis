from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class OneGameDataSaver(models.Model):
    class Meta:
        permissions = [('Can Record every game', 'Can Record every game'),
                       ('Can Update one game', 'Can Update one game'),
                       ('Can view game result', 'Can view game result')]

    recorder = models.CharField(max_length=50)
    RecordTime = models.DateTimeField(default='2021-12-01 00:00')
    SelectedPlayers = models.JSONField(default=dict)
    RoundsData = models.JSONField(default=dict)
    PlayerRoles = models.JSONField(default=dict)
    WinOrLoss = models.BooleanField(default=False)
    AfterMatch = models.JSONField(default=dict)


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    nickname = models.CharField(max_length=20, default='')
    # other statics data here.
    MerlinRounds = models.IntegerField(default=0)
    MerlinWins = models.IntegerField(default=0)
    PaiRounds = models.IntegerField(default=0)
    PaiWins = models.IntegerField(default=0)
    MogannaRounds = models.IntegerField(default=0)
    MogannaWins = models.IntegerField(default=0)
    BadRounds = models.IntegerField(default=0)
    BadWins = models.IntegerField(default=0)


class Seasons(models.Model):
    SeasonName = models.CharField(max_length=40, primary_key=True)
    SeasonStart = models.DateField(blank=True)
    SeasonEnd = models.DateField(blank=True)
    SeasonKing = models.CharField(max_length=40)
    SeasonDirtyKing1 = models.CharField(max_length=40)
    SeasonDirtyKing2 = models.CharField(max_length=40)
    SeasonDirtyKing3 = models.CharField(max_length=40)


class ScoreBoard(models.Model):
    season = models.ForeignKey(Seasons, on_delete=models.RESTRICT)
    player = models.ForeignKey(User, on_delete=models.RESTRICT)
    score = models.IntegerField(default=1000)


# class GamePlayer(models.Model):
#     username = models.CharField(max_length=40)
#     RealName = models.CharField(max_length=40)
#
#
# class GameRoles(models.Model):
#     RoleName = models.CharField(max_length=10)
#     RoleArmy = models.CharField(max_length=10)
#
#
# class OneSetGame(models.Model):
#     GameDate = models.DateTimeField("Game Played Date")
#     GamePlayers = models.JSONField("GamePlayer Sets")
#     GamePlayerNumber = models.IntegerField()
#     GameFinished = models.BooleanField("Game is in progress or not", default=False)
#     FinalResult = models.BooleanField("Winning or loose", default=False)
#     Recorder = models.ForeignKey(GamePlayer, on_delete=models.RESTRICT)
#     Killed = models.IntegerField("Killed player", null=True)
#
#
# class PlayerRoles(models.Model):
#     GameSetId = models.ForeignKey(OneSetGame, on_delete=models.RESTRICT)
#     GamePlayer = models.ForeignKey(GamePlayer, on_delete=models.RESTRICT)
#     PlayerRole = models.ForeignKey(GameRoles, on_delete=models.RESTRICT)
#     AnnouncedPAI = models.BooleanField(default=False)
#     DeAnnouncedPAI = models.BooleanField(default=False)
#     Winning = models.BooleanField(default=False)
#
#
# class GameRoundOne(models.Model):
#     GameSetId = models.ForeignKey(OneSetGame, on_delete=models.RESTRICT)
#     GameCarNumber = models.IntegerField()
#     GameCarPlayers = models.JSONField("Game Player Id sets for this round mission")
#     GameCarVotes = models.JSONField("Game Car votes for yes for this round mission")
#     GameCarResults = models.BooleanField(default=False)
#     DeniedCarOnePlayers = models.JSONField("Denied Car one players id set for this round")
#     DeniedCarOneVotes = models.JSONField("Car Votes for yes for denied car one")
#     DeniedCarTwoPlayers = models.JSONField("Denied Car two players id set for this round")
#     DeniedCarTwoVotes = models.JSONField("Car Votes for yes for denied car two")
#

