from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$', views.index),
        url(r'^new', views.new),
        url(r'^(?P<user_id>\d+)$', views.show),
        url(r'^(?P<user_id>\d+)/edit$', views.edit),
        url(r'^create', views.create),
        url(r'^(?P<user_id>\d+)/update$', views.update),
        url(r'^(?P<user_id>\d+)/destroy$', views.destroy),
]
