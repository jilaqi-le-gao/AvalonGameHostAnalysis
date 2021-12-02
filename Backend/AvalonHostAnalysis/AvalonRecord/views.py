from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import UserInfo
import json

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
    pass


def record_list_get(request):
    pass


def record_get_single(request):
    pass