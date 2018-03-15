from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': '127.0.0.1:6379',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'homepage',
        'USER': 'homepage'
    }
}

SECURE_CONTENT_TYPE_NOSNIFF=True
SECURE_BROWSER_XSS_FILTER=True
SECURE_SSL_REDIRECT=True
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True
X_FRAME_OPTIONS='DENY'

import os

STATIC_ROOT=os.path.join(BASE_DIR, "static/")
MEDIA_ROOT=os.path.join(BASE_DIR, "media/")
