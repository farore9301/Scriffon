from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from mysite.views import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', static_page, {'template': 'index'}),
	(r'^about/$', static_page, {'template': 'about'}),
	(r'^autorisation/', envoi_autorisation),
	(r'^admin/', include(admin.site.urls)),
)