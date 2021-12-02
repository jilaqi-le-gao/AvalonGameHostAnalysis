from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_csrftoken, name='csrf_token'),
    path('failed', views.not_logged_view, name='not logged'),
    path('just_logged', views.redirect_test_empty, name='just logged'),
]