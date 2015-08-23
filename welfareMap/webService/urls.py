from django.conf.urls import url
from webService import views


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^getUser/$', views.getUser, name='getUser'),
    url(r'^$', views.webService, name='webService'),
]