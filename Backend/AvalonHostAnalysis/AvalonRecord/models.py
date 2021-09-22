from django.db import models

# Create your models here.


class GamePlayer(models.Model):
    username = models.CharField(max_length=40)
    RealName = models.CharField(max_length=40)


class GameRoles(models.Model):
    RoleName = models.CharField(max_length=10)
    RoleArmy = models.CharField(max_length=10)


class OneSetGame(models.Model):
    GameDate = models.DateTimeField("Game Played Date")
    GamePlayers = models.JSONField("GamePlayer Sets")
    GamePlayerNumber = models.IntegerField()
    GameFinished = models.BooleanField("Game is in progress or not", default=False)
    FinalResult = models.BooleanField("Winning or loose", default=False)
    Recorder = models.ForeignKey(GamePlayer, on_delete=models.RESTRICT)
    Killed = models.IntegerField("Killed player", null=True)


class PlayerRoles(models.Model):
    GameSetId = models.ForeignKey(OneSetGame, on_delete=models.RESTRICT)
    GamePlayer = models.ForeignKey(GamePlayer, on_delete=models.RESTRICT)
    PlayerRole = models.ForeignKey(GameRoles, on_delete=models.RESTRICT)
    AnnouncedPAI = models.BooleanField(default=False)
    DeAnnouncedPAI = models.BooleanField(default=False)
    Winning = models.BooleanField(default=False)


class GameRoundOne(models.Model):
    GameSetId = models.ForeignKey(OneSetGame, on_delete=models.RESTRICT)
    GameCarNumber = models.IntegerField()
    GameCarPlayers = models.JSONField("Game Player Id sets for this round mission")
    GameCarVotes = models.JSONField("Game Car votes for yes for this round mission")
    GameCarResults = models.BooleanField(default=False)
    DeniedCarOnePlayers = models.JSONField("Denied Car one players id set for this round")
    DeniedCarOneVotes = models.JSONField("Car Votes for yes for denied car one")
    DeniedCarTwoPlayers = models.JSONField("Denied Car two players id set for this round")
    DeniedCarTwoVotes = models.JSONField("Car Votes for yes for denied car two")


