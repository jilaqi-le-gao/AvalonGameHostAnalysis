from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import UserInfo, OneGameDataSaver
import json
from django.conf import settings
from django.http import Http404

# Create your views here.


def hello_world(request):
    return HttpResponse("hello world!")


def get_all_players(request):
    all_users = User.objects.all()
    ret = []
    for one_user in all_users:
        ret.append(one_user.username)
    return HttpResponse(json.dumps(ret, ensure_ascii=False).encode('utf8'))


def record_post(request):
    request_body = json.loads(request.body.decode('utf-8'))
    this_record = OneGameDataSaver(recorder=request_body['Recoder'])
    this_record.SelectedPlayers = request_body['SelectedPlayers']
    this_record.RoundsData = request_body['RoundsData']
    this_record.PlayerRoles = request_body['PlayerRoles']
    this_record.WinOrLoss = request_body['WinOrLoss']
    this_record.AfterMatch = request_body['AfterMatch']
    record_id = this_record.save()
    ret_struct = {
        'flag': True,
        'record_id': record_id,
        'next_url': '/sibyl/page/RecordView'
    }
    return HttpResponse(json.dumps(ret_struct))


def get_current_user(request):
    if not settings.FAKE_AUTH:
        if request.user.is_authenticated:
            username = request.user.get_username()
        else:
            raise Http404("not authed!")
    else:
        username = 'gaole'
    return HttpResponse(username)


def record_list_get(request):
    pass


def record_get_single(request):
    pass