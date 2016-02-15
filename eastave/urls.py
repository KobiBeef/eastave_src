from django.conf.urls import include, patterns, url
from django.contrib import admin

urlpatterns = patterns(
	'',
    # Examples:
    # url(r'^$', 'eastave.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # core urls
    url(r'^admin/', include(admin.site.urls)),

    # project urls
    url(r'denzo/', include("denzo.urls")),
)