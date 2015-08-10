from django.conf.urls import url


from about import views


urlpatterns = [
    url(r'^idea/$', views.idea, name='idea'),
    url(r'^introduction/$', views.introduction, name='introduction'),
    url(r'^use/$', views.use, name='use'),
    url(r'^aboutUs/$', views.aboutUs, name='aboutUs'),
    url(r'^$', views.about, name='about'),
]
