#blog urls
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name = 'blog'),
    url(r'^view/(?P<slug>[^\.]+).html', views.PostView.as_view(), name='view_post'),
    url(r'^category/(?P<slug>[^\.]+).html', views.CategoryView.as_view(), name='view_category'),
    url(r'^tag/(?P<slug>[^\.]+).html', views.TagView.as_view(), name='view_tag'),
    url(r'^new/', views.post_new, name='post_new'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]
