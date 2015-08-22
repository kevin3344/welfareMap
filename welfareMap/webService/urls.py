from django.conf.urls import url
from webService import views


urlpatterns = [
    url(r'^$', views.webService, name='webService'),
]