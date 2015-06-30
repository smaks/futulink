#blog urls
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name = 'blog'),
    url(r'^view/(?P<slug>[^\.]+).html', views.PostView.as_view(), name='view_post'),
    url(r'^category/(?P<slug>[^\.]+).html', views.CategoryView.as_view(), name='view_category'),
]
