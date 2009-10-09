# -*- coding: utf-8 -*-
from ragendja.settings_pre import *

MEDIA_VERSION = 1

# Change your email settings
if on_production_server:
    DEFAULT_FROM_EMAIL = 'youremail@gmail.com' # make sure this is an admin email on your app so you receive error messages
    SERVER_EMAIL = DEFAULT_FROM_EMAIL
else:
    ENABLE_PROFILER = True
    ONLY_FORCED_PROFILE = True
    PROFILE_PERCENTAGE = 25
    SORT_PROFILE_RESULTS_BY = 'cumulative' # default is 'time'
    # Profile only datastore calls
    #PROFILE_PATTERN = 'ext.db..+\((?:get|get_by_key_name|fetch|count|put)\)'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '123456789yoursecretkey'

# Enable I18N and set default language to 'en'
USE_I18N = True
LANGUAGE_CODE = 'en'

# Restrict supported languages (and JS media generation)
LANGUAGES = (
    ('en', 'English'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
)

MIDDLEWARE_CLASSES = (
    'ragendja.middleware.ErrorMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'ragendja.sites.dynamicsite.DynamicSiteIDMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)


LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'
LOGIN_REDIRECT_URL = '/'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.webdesign',
    'django.contrib.flatpages',
    'django.contrib.redirects',
    'django.contrib.sites',
    'appenginepatcher',
    'ragendja',
    'superfeedr_api',
)

# List apps which should be left out from app settings and urlsauto loading
IGNORE_APP_SETTINGS = IGNORE_APP_URLSAUTO = ()

# Remote access to production server (e.g., via manage.py shell --remote)
DATABASE_OPTIONS = {}

SUPERFEEDR_USERNAME = ''
SUPERFEEDR_PASSWORD = ''
SUPERFEEDR_HUB  = 'http://superfeedr.com/hubbub'
SUPERFEEDR_CALLBACK = 'gae-superfeedr-shell.appspot.com/api/superfeedr/receive_feeds/'

from ragendja.settings_post import *
