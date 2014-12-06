from django.conf.urls import patterns, include, url

urlpatterns = patterns('recruit.frontend.views',
    url(r'^$', 'home', name='home'),
)