from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
                 url(r'^$', 'user.views.home', name='home'),
                 url(r'^login/$', 'user.views.user_login', name='login'),
                 url(r'^logout/$', 'django.contrib.auth.views.logout',
                     name='logout_page'),
                 url(r'^register/$', 'user.views.register', 
                     name="register"),
)

