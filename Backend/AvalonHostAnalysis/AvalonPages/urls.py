from django.urls import path

from . import views

urlpatterns = [
    path('RecordGame/', views.RecordGamePage, name='RecordGame page'),
]