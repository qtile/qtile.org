import os
from memcacheify import memcacheify
from .common import *

# Allowed Hosts
ALLOWED_HOSTS = ['.herokuapp.com']
if 'ALLOWED_HOSTS' in os.environ:
    ALLOWED_HOSTS.extend(os.environ['ALLOWED_HOSTS'].split(','))

# Cache
CACHES = memcacheify()

# django-compressor
COMPRESS_ENABLED = True

# Sentry - error logging service
if 'SENTRY_DSN' in os.environ:
    import sentry_sdk
    sentry_sdk.init(os.environ['SENTRY_DSN'])
