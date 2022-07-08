from .base import *

DEBUG = False

ALLOWED_HOSTS = ['tecnoelectrocomercioonline.com']

# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS SETTINGS
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_RELOAD = True
SECURE_HSTS_SUBDOMAINS = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=120)
}

# PostgreSQL / MySQL dB: PROD
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': config('HEROKUPOSTGRESQL_HOST'),
#         'NAME': config('HEROKUPOSTGRESQL_NAME'),
#         'USER': config('HEROKUPOSTGRESQL_USER'),
#         'PASSWORD': config('HEROKUPOSTGRESQL_PASSWORD'),
#         'PORT': '5432'
#     }
# }

# Redis caching
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get('REDISCLOUD_URL'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# CSS, JS, Images
STATIC_URL = '/static/'

#static files for templates
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Collects the static files into STATIC_ROOT (AWS S3) For Example 
# & search for all the static files on your system and move them here
# STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_ROOT = os.path.join(BASE_DIR, 'live-static-files', 'static-root')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'live-static-files', 'media-root')

# Help us serves StaticFiles in Prod
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
