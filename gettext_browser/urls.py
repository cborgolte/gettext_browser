from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^poentry/$', 'gettext_browser.views.show', name='showentry'),
    # for production use a more complicated url, like
    #url(r'^iesheeNg4Ithaithi9ATaeNgievohP/$', 'gettext_browser.views.show', name='showentry'),
)
