from django.contrib import admin

from superfeedr_api.models import SuperFeedrActivity

from django import forms
from django.conf import settings
from django.template.defaultfilters import slugify


class SuperFeedrActivityAdmin(admin.ModelAdmin):
    exclude = ['activity_counter'] 
    list_display = ('created','processed','type',)
    list_filter = ('processed','type',)
    ordering       = ('-created',)
    pass

admin.site.register(SuperFeedrActivity, SuperFeedrActivityAdmin)

