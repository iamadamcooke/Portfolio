from django.conf.urls import patterns, include, url
from rss.feeds import RSSFeed

urlpatterns = patterns('',
    url(r'^admin/', include('admin.urls')),
    url(r'^$', 'itsme.views.about'),
    url(r'^sitemap\.xml$', 'itsme.views.sitemap'),
    url(r'^feed/$', RSSFeed()),
    url(r'^page/(?P<page>\d+)/$', 'itsme.views.blog'),
    url(r'^blog/$', 'itsme.views.blog'),
    url(r'^blog/(?P<slug>[\w-]+)/$', 'itsme.views.post_view'),
    url(r'^work/$', 'itsme.views.work'),
    url(r'^about/$', 'itsme.views.about'),
    url(r'^contact/$', 'itsme.views.contact'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/Users/adamcooke/Code/Personal/Portfolio/static', 'show_indexes': True}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/Users/adamcooke/Code/Personal/Portfolio/media', 'show_indexes': True}),
)