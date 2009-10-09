from google.appengine.ext import db
from google.appengine.api import memcache

from superfeedr_api.models import SuperFeedrActivity 

def get_activity_count():
    try:
        f = SuperFeedrActivity.all()
        f.order('-activity_counter')
        activity = f[0]
        return int(activity.activity_counter)
    except:
        return 0
