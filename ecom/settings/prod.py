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