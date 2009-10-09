from django.conf.urls.defaults import *

from superfeedr_api import views as api_views

urlpatterns = patterns('',
    url(r'^receive_feeds/', api_views.receive_feeds, name="api-receive_feeds"),
    url(r'^add_feed_subscription/', api_views.add_feed_subscription, name="api-add_feed_subscription"),
    url(r'^view_superfeedr_updates/', api_views.view_superfeedr_updates, name="api-view_superfeedr_updates"),
    )

