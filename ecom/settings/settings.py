from .base import *
import django_heroku

ROOT_URLCONF = 'ecom.urls'

WSGI_APPLICATION = 'ecom.wsgi.application'

django_heroku.settings(locals())