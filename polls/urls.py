from django.conf.urls import patterns
from django.conf.urls import url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^/suggestions/$', views.suggestionView, name='suggestions'),
    url(r'^/uploadSuggestion/$', views.uploadSuggestion, name='uploadSuggestion'),



)
