from .base import *
import os
import datetime

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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': config('HEROKUPOSTGRESQL_HOST'),
        'NAME': config('HEROKUPOSTGRESQL_NAME'),
        'USER': config('HEROKUPOSTGRESQL_USER'),
        'PASSWORD': config('HEROKUPOSTGRESQL_PASSWORD'),
        'PORT': '5432'
    }
}

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

# AWS RDS AND S3 Config
  
# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# AWS_LOCATION = 'static'
# AWS_DEFAULT_ACL = None
# AWS_S3_FILE_OVERWRITE = False
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DEFAULT_FILE_STORAGE = 'myapp.storages.MediaStorage'