from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.list_of_post, name="post_list"),
    url(r'^blog$', views.blog_list, name="blog_list"),
    #url(r'^(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^blog/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^blog/category/(?P<category_slug>[-\w]+)/$', views.list_of_post_by_category , name='list_of_post_by_category'),
    url(r'^blog/(?P<slug>[-\w]+)/comment/$', views.add_comment,  name='add_comment'),
    url(r'^backend/post/new/$', views.new_post, name='new_post'),
    url(r'^backend/post/$', views.list_of_post_backend, name='list_of_post_backend'),
    url(r'^backend/(?P<slug>[-\w]+)/edit/$', views.edit_post, name='edit_post'),
    url(r'^backend/(?P<slug>[-\w]+)/delete/$', views.delete_post, name='delete_post'),
    
    
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name="post_detail"),
    #url(r'^post/new/$', views.post_new, name='post_new'), # Url editar los post
    #url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    #url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    #url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    #url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    #url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    #url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    #url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    
    #url(r'^category/$', views.category, name='category'),
    #url(r'^category/(?P<pk>\d+)/detail/$', views.category_detail, name='category-detail'),
]

