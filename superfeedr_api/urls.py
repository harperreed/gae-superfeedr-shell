from django.conf.urls.defaults import *

from superfeedr_api import views as api_views

urlpatterns = patterns('',
    url(r'^receive_feeds/', api_views.receive_feeds, name="api-receive_feeds"),
    )

