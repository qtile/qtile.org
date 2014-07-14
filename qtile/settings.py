"""
Django settings for qtile.org.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
import sys
from memcacheify import memcacheify

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ln-=_^uq_8_5qf3fi^00y(lckyz(d31h^o!8m+f_+#xo=w7!u^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DJANGO_DEBUG', 1)))

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

ALLOWED_INCLUDE_ROOTS = [
    os.path.join(PROJECT_DIR, 'includes')
]

# Application definition

INSTALLED_APPS = (
    'django.contrib.staticfiles',

    'qtile',

    'compressor',
    'django_pygments',
    'jsonify',
    'raven.contrib.django'
)

MIDDLEWARE_CLASSES = (
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'qtile.urls'

WSGI_APPLICATION = 'qtile.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {}

# Cache
# https://docs.djangoproject.com/en/1.6/ref/settings/#caches

CACHES = memcacheify()

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

# if 'collectstatic' not in sys.argv:
STATICFILES_DIRS.append(os.path.join(BASE_DIR, 'public/bower_components'))

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')

# django-compressor
# http://django-compressor.readthedocs.org

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc -x {infile} {outfile}'),
)

# Templating

TEMPLATE_DIRS = (os.path.join(PROJECT_DIR, 'templates'),)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'qtile.context_processors.context',
)

# Sentry - error logging service

if 'SENTRY_DSN' in os.environ:
    RAVEN_CONFIG = {
        'dsn': os.environ['SENTRY_DSN'],
        'register_signals': True,
    }
    RAVEN_PUBLIC_DSN = 'https://public@{0}'.format(RAVEN_CONFIG['dsn'].split('@')[1])

# Qtile Stuff

QTILE_VERSION = os.environ.get('QTILE_VERSION', '0.7.0')

QTILE_DOWNLOAD = os.environ.get('QTILE_DOWNLOAD',
    'https://github.com/qtile/qtile/archive/v{0}.tar.gz'.format(QTILE_VERSION))

QTILE_RELEASE_NOTES = os.environ.get('QTILE_RELEASE_NOTES',
    'http://docs.qtile.org/en/latest/releases/{0}.html'.format(QTILE_VERSION))
