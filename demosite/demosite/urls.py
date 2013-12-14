from django.conf.urls import patterns, include, url
from demosite.views import hello,create_time,hours_ahead

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demosite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^hello/$', hello),
	url(r'^time/$', create_time),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
