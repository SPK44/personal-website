from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
	# ex: /blog/
	url(r'^$', views.index, name='index'),
	# ex: /blog/4/
	url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
	# ex: /blog/contact/
	url(r'^contact/$', views.contact , name='contact'),
]
