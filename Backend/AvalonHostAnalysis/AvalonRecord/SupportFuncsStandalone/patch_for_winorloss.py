from AvalonRecord.models import *
data = OneGameDataSaver.objects.all()

for one_game in data:
    print('processing', one_game)
    for one_set in one_game.RoundsData:
        if not 'VoteResultFailNumber' in one_set:
            continue
        if one_set['VoteResultFailNumber'] is not None:
            if one_set['VoteResultFailNumber'] > 0:
                one_set['WinOrLoss'] = False
            else:
                one_set['WinOrLoss'] = True
    one_game.save()
