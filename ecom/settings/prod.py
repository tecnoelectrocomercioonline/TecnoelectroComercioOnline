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
        # 'ENGINE':'django.db.backends.postgresql_psycopg2', #If ERRORS USE THIS
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': config('HEROKUPOSTGRESQL_HOST'),
        'NAME': config('HEROKUPOSTGRESQL_NAME'),
        'USER': config('HEROKUPOSTGRESQL_USER'),
        'PASSWORD': config('HEROKUPOSTGRESQL_PASSWORD'),
        'PORT': '5432'
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redis caching
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": os.environ.get('REDISCLOUD_URL'),
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# STATICFILES_DIRS = [BASE_DIR / 'static',]

# MEDIA_URL = '/images/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# # STATICFILES_DIRS = [BASE_DIR / 'static',]
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
# MEDIA_ROOT = BASE_DIR / 'mediafiles'

# PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# STATIC_ROOT  =   os.path.join(PROJECT_ROOT, 'staticfiles')

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