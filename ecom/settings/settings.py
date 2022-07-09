from .base import *
import django_heroku

WSGI_APPLICATION = 'ecom.wsgi.application'

django_heroku.settings(locals())