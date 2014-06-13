from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    # Login / logout.
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$','user.views.bye', name='logout_page'),

)
