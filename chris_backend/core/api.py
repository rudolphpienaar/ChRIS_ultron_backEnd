from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from feeds import views


# API v1 endpoints
urlpatterns = format_suffix_patterns([
    
    url(r'^v1/$', views.FeedList.as_view(), name='feed-list'),
    
    url(r'^v1/(?P<pk>[0-9]+)/$',
        views.FeedDetail.as_view(), name='feed-detail'),
    
    url(r'^v1/note(?P<pk>[0-9]+)/$',
        views.NoteDetail.as_view(), name='note-detail'),
    
    url(r'^v1/(?P<pk>[0-9]+)/tags/$',
        views.TagList.as_view(), name='tag-list'),

    url(r'^v1/tags/(?P<pk>[0-9]+)/$',
        views.TagDetail.as_view(), name='tag-detail'),
    
    url(r'^v1/(?P<pk>[0-9]+)/comments/$',
        views.CommentList.as_view(), name='comment-list'),
    
    url(r'^v1/comments/(?P<pk>[0-9]+)/$',
        views.CommentDetail.as_view(), name='comment-detail'),
    
    url(r'^v1/(?P<pk>[0-9]+)/files/$',
        views.FeedFileList.as_view(), name='feedfile-list'),

    url(r'^v1/files/(?P<pk>[0-9]+)/$',
        views.FeedFileDetail.as_view(), name='feedfile-detail'),

    url(r'^v1/files/(?P<pk>[0-9]+)/.*$',
        views.FileResource.as_view(), name='file-resource'), 

])

# Login and logout views for Djangos' browsable API
urlpatterns += [
    url(r'^v1/auth/', include('rest_framework.urls',  namespace='rest_framework')),
]

