from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
