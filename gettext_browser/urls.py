from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^poentry/$', 'gettext_browser.views.show', name='showentry'),
)
