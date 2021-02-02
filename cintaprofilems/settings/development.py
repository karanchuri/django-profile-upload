from .base import *

DEBUG = True
FLAVOUR = "dev"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB', 'cintaprofile'),
        'USER': os.environ.get('POSTGRES_USER', 'cinta'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'YfDBOXDuc7PjWa32xqkhbSU0kS7yX6m5'),
        'HOST': os.environ.get('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
        'CONN_MAX_AGE': None,
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 1,  # in seconds
            "SOCKET_TIMEOUT": 1,  # in seconds
        },
        "KEY_PREFIX": "cinta_profile",
    }
}
