from django.conf.urls import url

from supply import views


urlpatterns = [
    url(r'^List/$', views.supplyList, name='supplyList'),
    url(r'^$', views.supplyMap, name='supplyMap'),
]