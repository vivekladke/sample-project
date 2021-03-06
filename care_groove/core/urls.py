from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
