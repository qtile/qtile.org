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
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=os.environ['SENTRY_DSN'],
        integrations=[DjangoIntegration()]
    )
