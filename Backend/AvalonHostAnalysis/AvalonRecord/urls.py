from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.hello_world, name='index'),
    path('GetUsername/', views.get_current_user),
    path('GetAllPlayers/', views.get_all_players),
    path('SaveGameRecord/', views.record_post),
]