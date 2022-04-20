from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Redis caching
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": os.path.join(BASE_DIR, 'cache'),
        "LOCATION": "redis://127.0.0.1:6379/1",
        # "LOCATION": "redis://:p18c919c90eba2539dd800c349d49e118c17e1a782f474db85693484d53bb96ee@ec2-3-230-177-186.compute-1.amazonaws.com:10380",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False