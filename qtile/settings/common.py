"""
Django settings for qtile.org.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import datetime
import os

from unipath import Path

# Build paths inside the project like this: BASE_DIR.child(...)
BASE_DIR = Path(__file__).absolute().ancestor(3)
PROJECT_DIR = Path(__file__).absolute().ancestor(2)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DJANGO_DEBUG', 1)))

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

ALLOWED_INCLUDE_ROOTS = [
    os.path.join(PROJECT_DIR, 'includes')
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.staticfiles',

    'qtile',

    'compressor',
    'django_pygments',
    'jsonify',
    'raven.contrib.django.raven_compat',
]

MIDDLEWARE = [
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'qtile.urls'

WSGI_APPLICATION = 'qtile.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {}

# Cache
# https://docs.djangoproject.com/en/1.6/ref/settings/#caches

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

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
    PROJECT_DIR.child('static'),
    BASE_DIR.child('public', 'bower_components'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
]

STATIC_ROOT = BASE_DIR.child('public', 'static')

# django-compressor
# http://django-compressor.readthedocs.org

COMPRESS_ENABLED = False
COMPRESS_OFFLINE = True
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc --js -x {infile} {outfile}'),
)

# Templating

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'qtile.context_processors.context',
            ],
        },
    },
]


# Qtile Stuff

QTILE_VERSION = os.environ.get('QTILE_VERSION', '0.10.4')

QTILE_DOWNLOAD = os.environ.get('QTILE_DOWNLOAD',
    'https://github.com/qtile/qtile/archive/v{0}.tar.gz'.format(QTILE_VERSION))

QTILE_RELEASE_DATE = datetime.datetime.strptime(
    os.environ.get('QTILE_RELEASE_DATE', '2016-01-19'), '%Y-%m-%d').date()


# Google Analytics Tracking ID

GOOGLE_ANALYTICS_ID = os.environ.get('GOOGLE_ANALYTICS_ID')
