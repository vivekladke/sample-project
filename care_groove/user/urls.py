from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns(
    '',
    # Login / logout.
    #url(r'^$', 'user.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="logout"),
    url(r'^register/$', 'user.views.register', name='register'),
)
