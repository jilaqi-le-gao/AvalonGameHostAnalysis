from django.shortcuts import render
from django.middleware.csrf import get_token
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def get_csrftoken(request):
    token = get_token(request)
    return JsonResponse({
        'csrftoken': token
    })


@login_required
def redirect_test_empty(request):
    print(request.user)
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return HttpResponse('You are logged in!')
    else:
        # Do something for anonymous users.
        return HttpResponse('You are NOT logged in!')


def not_logged_view(request):
    if request.user.is_authenticated():
        print(request.user.get_username())
    return HttpResponse('You are not logged in !!!')
