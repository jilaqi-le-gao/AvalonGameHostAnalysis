import numpy as np


def calculate_game_weight(win_rounds, loss_rounds, num_players):
    if num_players == 10:
        player_weight = 1
    else:
        player_weight = 0.8

    if win_rounds == 0:
        car_weight = 0.6
    elif loss_rounds == 0:
        car_weight = 0.5
    elif win_rounds == 1 and loss_rounds >= 1:
        car_weight = 0.8
    elif loss_rounds == 1 and win_rounds >= 1:
        car_weight = 0.8
    else:
        car_weight = 1

    return car_weight * 0.7 + player_weight * 0.3


def calculate_win_loss_sets(RoundsData):
    win = 0
    loss = 0
    for one_round in RoundsData:
        if one_round['WinOrLoss']:
            win += 1
        else:
            loss += 1

        if win >= 3 or loss >= 3:
            break

    return win, loss


def calculate_key_chara_score(PlayerRoles, AfterMatch, PlayerScores):
    if AfterMatch['Kill'] != '':
        if PlayerRoles['Merlin']['Player'] == AfterMatch['Kill']:
            # 刀中了
            PlayerScores[PlayerRoles['Assassin']['Player']] += 10
        elif PlayerRoles['Pai']['Player'] == AfterMatch['Kill']:
            # 刀了派
            PlayerScores[PlayerRoles['Pai']['Player']] += 20
        else:
            PlayerScores[AfterMatch['Kill']] += 40
    return PlayerScores


def init_win_loss_base_score(PlayerScores, WinOrLoss, PlayerRoles):
    if WinOrLoss:
        if PlayerRoles['Morgana']['Player'] != '':
            PlayerScores[PlayerRoles['Morgana']['Player']] -= 50
        if PlayerRoles['Assassin']['Player'] != '':
            PlayerScores[PlayerRoles['Assassin']['Player']] -= 50
        if PlayerRoles['BadGuy']['Player'] != '':
            PlayerScores[PlayerRoles['BadGuy']['Player']] -= 50
        if PlayerRoles['Aobolun']['Player'] != '':
            PlayerScores[PlayerRoles['Aobolun']['Player']] -= 50
        if PlayerRoles['Modeleide']['Player'] != '':
            PlayerScores[PlayerRoles['Modeleide']['Player']] -= 50

        for OnePlayer in PlayerScores:
            if PlayerScores[OnePlayer] == 0:
                PlayerScores[OnePlayer] += 50
    else:
        if PlayerRoles['Morgana']['Player'] != '':
            PlayerScores[PlayerRoles['Morgana']['Player']] += 50
        if PlayerRoles['Assassin']['Player'] != '':
            PlayerScores[PlayerRoles['Assassin']['Player']] += 50
        if PlayerRoles['BadGuy']['Player'] != '':
            PlayerScores[PlayerRoles['BadGuy']['Player']] += 50
        if PlayerRoles['Aobolun']['Player'] != '':
            PlayerScores[PlayerRoles['Aobolun']['Player']] += 50
        if PlayerRoles['Modeleide']['Player'] != '':
            PlayerScores[PlayerRoles['Modeleide']['Player']] += 50

        for OnePlayer in PlayerScores:
            if PlayerScores[OnePlayer] == 0:
                PlayerScores[OnePlayer] -= 50

    return PlayerScores


def calculate_score(one_game_info):
    PlayerScores = {}
    for one_player in one_game_info.SelectedPlayers:
        PlayerScores[one_player] = 0

    PlayerScores = init_win_loss_base_score(PlayerScores, one_game_info.WinOrLoss, one_game_info.PlayerRoles)

    win_round, loss_round = calculate_win_loss_sets(one_game_info.RoundsData)
    print(win_round, loss_round)

    game_weight = calculate_game_weight(win_round, loss_round, len(one_game_info.SelectedPlayers))
    print(game_weight)

    PlayerScores = calculate_key_chara_score(one_game_info.PlayerRoles, one_game_info.AfterMatch, PlayerScores)
    print(PlayerScores)

    return PlayerScores
