from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.hello_world, name='index'),
    path('GetAllPlayers/', views.get_all_players),

]