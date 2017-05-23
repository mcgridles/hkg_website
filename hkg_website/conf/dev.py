import os
from base import *

DEBUG = True

ALLOWED_HOSTS = [
    'hkg-website.herokuapp.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}
