__author__ = 'ben'
from django.conf.urls import patterns, include, url
from .views import (PostCreateView, PostDeleteView, PostDetailView,
                    PostListView, PostUpdateView)

urlpatterns = patterns('',
    url(r'^create/$', PostCreateView.as_view(), name='create_post'),
    url(r'^update/(?P<slug>[\w\d_-]+)/$', PostUpdateView.as_view(),
        name='update_post'),
    url(r'^delete/(?P<slug>[\w\d_-]+)/$', PostDeleteView.as_view(),
        name='delete_post'),
    url(r'^post/(?P<slug>[\w\d_-]+)/$', PostDetailView.as_view(),
        name='detail_post'),
    url(r'^$', PostListView.as_view(), name='list_posts'),
)
