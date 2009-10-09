# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from google.appengine.ext import db

from google.appengine.ext import search 
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


class SuperFeedrActivity(db.Model):
    update = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add=True)

    processed = db.BooleanProperty()
    type = db.StringProperty()

    activity_counter =  db.IntegerProperty()

    class Meta:
        verbose_name_plural = 'SuperFeedr activities'
            
    def __unicode__(self):
        return u'activity: %s' % (self.created) 

