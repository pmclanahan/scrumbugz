from __future__ import absolute_import

import json
import os

import dj_database_url

from .base import *


SERVICES = json.loads(os.getenv('VCAP_SERVICES', '[]'))
SITE_URL = 'http://scrumbugz.paas.allizom.org'

ADMINS = (
    ('Paul', 'pmac@mozilla.com'),
)
MANAGERS = ADMINS

DATABASES = {'default': dj_database_url.config()}

SECRET_KEY = os.getenv('SECRET_KEY', 'ssssssssshhhhhhhhhhhh')

if 'REDIS_URL' in os.environ:
    # Celery
    BROKER_URL = os.environ['REDIS_URL']
    CELERY_RESULT_BACKEND = BROKER_URL

if 'MEMCACHE_URL' in os.environ:
    memcache = SERVICES['memcached'][0]['credentials']
    os.environ['MEMCACHE_SERVERS'] = os.environ['MEMCACHE_URL']
    #os.environ['MEMCACHE_USERNAME'] = memcache['user']
    #os.environ['MEMCACHE_PASSWORD'] = memcache['password']
