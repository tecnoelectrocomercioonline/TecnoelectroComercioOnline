from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost']

# SQLlite DB 
# DATABASES = {
#     'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# PostgreSQL / MySQL DB: Local Dev
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': config('POSTGRES_HOST_DEV'),
#         'NAME': config('POSTGRES_NAME_DEV'),
#         'USER': config('POSTGRES_USER_DEV'),
#         'PASSWORD': config('POSTGRES_PASSWORD_DEV'),
#         'PORT': '5432'
#     }
# }

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

