from django.conf.urls import patterns, include, url
from demosite.views import hello,current_datetime,hours_ahead,display_meta
from demosite.books.views import search_form,search
from demosite.contact.views import contact,thanks

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demosite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^hello/$', hello),
	url(r'^time/$', current_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	url(r'^meta/$', display_meta),
	url(r'^search-form/$',search_form),
	url(r'^search/$',search),
	url(r'^contact/$',contact),
	url(r'^contact/thanks/$', thanks),
)
