from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name="post_detail"),
    url(r'^post/new/$', views.post_new, name='post_new'), # Url editar los post
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),


]