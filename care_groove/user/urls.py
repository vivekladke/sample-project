from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns(
    '',
    # Login / logout.
    url(r'^$', 'user.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout',
        {'next_page': '/login/'}, name='logout'),
    #url(r'^logout/$', 'user.views.bye', name='logout_page'),
    url(r'^register/$', 'user.views.register', name='register'),

)
