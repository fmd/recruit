from django.conf.urls import patterns, include, url
from django.contrib import admin
import recruit.frontend.urls as frontend


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recruit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


from django.conf import settings
from django.conf.urls.static import static
#Admin
urlpatterns = patterns('',
    url(r'^admin/',     include(admin.site.urls)),
    url(r'^',           include(frontend,  namespace = 'frontend')),
)