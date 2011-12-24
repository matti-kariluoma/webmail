from django.conf.urls.defaults import patterns, include, url
from django_localwebmail import webmail_data

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^unnamed_webmail/', include('unnamed_webmail.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

   url(r'^$', 'webmail_data.views.login'),
   url(r'^mail/(?P<folder>[a-z_]+)$', 'webmail_data.views.mail')
)
