from django.conf.urls import url
from userLogin import views


urlpatterns = [
    url(r'^userLogout/$', views.userLogout, name='userLogout'),
    url(r'^$', views.userLogin, name='userLogin'),
]