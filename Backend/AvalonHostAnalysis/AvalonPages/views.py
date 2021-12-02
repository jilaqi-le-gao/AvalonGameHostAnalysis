from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.


@login_required(login_url='/sibyl/login/')
def RecordGamePage(request):
    return render(request, 'FRONTEND/GameRecordPage.html', )


@login_required(login_url='/sibyl/login/')
def RecordViewPage(request):
    return HttpResponse('In progress')