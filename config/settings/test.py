__author__ = 'chedv13'

from .common import *

INSTALLED_APPS += ('django_nose',)

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'taskbox',
        'USER': 'taskbox',
        'PASSWORD': 'e4249G20WW4V2de',
        'HOST': '',
        'PORT': ''
    }
}

# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
