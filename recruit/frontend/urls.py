from django.conf.urls import patterns, include, url

urlpatterns = patterns('recruit.frontend.views',
    url(r'^test/([\w]{1,255})/([\w.%+-]{1,255})/([\d]{8})$', 'test', name='test'),
)