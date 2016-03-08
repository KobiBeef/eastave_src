from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns(
	'',
	url(r'^$', views.TestView.as_view(), name='index'),
	# url(r'^$', views.index, name='index'),
)