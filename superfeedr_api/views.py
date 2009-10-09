# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponsePermanentRedirect

from django.utils.translation import ugettext as _
from ragendja.template import render_to_response

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from django.contrib.sites.models import Site
from django.utils.encoding import smart_str, smart_unicode
from django.contrib.auth.decorators import login_required
from django.template import Context, loader
from django.core.urlresolvers import reverse


from django.conf import settings
from django.utils.translation import ugettext as _

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.api import memcache
from google.appengine.api import images
from google.appengine.api import urlfetch
from google.appengine.api import mail

from django.template.defaultfilters import slugify

from superfeedr_api.models import SuperFeedrActivity

from google.appengine.api.labs import taskqueue

from django.utils import simplejson

from google.appengine.api import xmpp

import logging
import datetime
import urllib
import random
import time
import datetime
import base64

import feedparser

import counter_helper

def superfeed_pubsubhubbub(post_data):
    base64string = base64.encodestring('%s:%s' % (settings.SUPERFEEDR_USERNAME, settings.SUPERFEEDR_PASSWORD))[:-1]
    form_data = urllib.urlencode(post_data)
    try:
        result = urlfetch.fetch(url=settings.SUPERFEEDR_HUB,
                        payload=form_data,
                        method=urlfetch.POST,
                        headers={"Authorization": "Basic "+ base64string, 'Content-Type': 'application/x-www-form-urlencoded'})
        if result.status_code == 200:
            print "asd"
            logging.debug(result)
            print "awesome"
        logging.debug(result.status_code)
    except:
        print "blah"

def add_feed_superfeedr(subscribe_feed):
    form_fields = {
        'hub.mode' : 'subscribe',
        'hub.callback' : settings.SUPERFEEDR_CALLBACK,
        'hub.topic' : subscribe_feed, 
        'hub.verify' : 'sync',
        'hub.verify_token' : '',
    }
    superfeed_pubsubhubbub(form_fields)

def remove_feed_superfeedr(subscribe_feed):
    form_fields = {
        'hub.mode' : 'unsubscribe',
        'hub.callback' : settings.SUPERFEEDR_CALLBACK,
        'hub.topic' : subscribe_feed, 
        'hub.verify' : 'sync',
        'hub.verify_token' : '',
    }
    superfeed_pubsubhubbub(form_fields)

def receive_feeds(request):
    logging.info('receiving feed')
    if request.GET:
        logging.debug('#authenticating feed')
        challenge = request.GET.get('hub.challenge')
        return HttpResponse(challenge)
    if request.raw_post_data:
        logging.debug('#saving feed data')
        data = request.raw_post_data
        logging.debug(data)
        a = SuperFeedrActivity()
        a.update = data
        a.activity_counter = int(counter_helper.get_activity_count()) +1
        a.save()
        logging.debug('#launching feed task')
	#do something with your feed update (this is will i queue a task to parse it)
        #taskqueue.Task(url=reverse("api-parse-feed-update"), params={'id': a.id}).add(queue_name='feedparsing')
        return HttpResponse('')
    logging.debug('Nope')
    return HttpResponse('hub.receive')

