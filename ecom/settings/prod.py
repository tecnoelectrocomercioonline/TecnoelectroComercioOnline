from .base import *

DEBUG = False
ALLOWED_HOSTS = ['tecnoelectroco.herokuapp.com']
# ALLOWED_HOSTS = ['tecnoelectrocomercioonline.com']

# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS SETTINGS
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_RELOAD = True
SECURE_HSTS_SUBDOMAINS = True
