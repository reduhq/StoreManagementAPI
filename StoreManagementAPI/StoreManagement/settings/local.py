from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:5173',
    'http://localhost:5173',
)

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '127.0.0.1:5173'
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'StoreManagementDB',
        'USER': 'sa',
        'PASSWORD': '12345678',
        'HOST': 'db',
        'PORT': '5432'
        # 'OPTIONS': {
        #     'driver': 'asyncpg',
        # },
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
