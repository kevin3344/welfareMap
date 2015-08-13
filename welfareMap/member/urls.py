from django.conf.urls import url
from member import views


urlpatterns = [
    url(r'^supplyNum/$', views.supplyNum, name='supplyNum'),
    url(r'^welfareNum/$', views.welfareNum, name='welfareNum'),
    url(r'^manager/$', views.manager, name='manager'),
    url(r'^member/$', views.member, name='member'),
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.member, name='member'),
]