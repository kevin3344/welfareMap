from django.conf.urls import url
from welfare import views


urlpatterns = [
    url(r'^(?P<index>\w+)/$', views.welfare, name='welfareIndex'),
    url(r'^$', views.welfare, name='welfare'),
]