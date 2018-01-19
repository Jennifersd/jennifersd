from django.conf.urls import patterns, url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
