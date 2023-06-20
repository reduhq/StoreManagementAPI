from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

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
