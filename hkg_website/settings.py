"""
Django settings for hkg_website project.
Generated by 'django-admin startproject' using Django 1.11.

Project created by Henry Gridley
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = [
    'www.henrygridley.me',
    'hkg-website.herokuapp.com',
]

ADMINS = (
    ('Henry Gridley', os.environ['HKG_EMAIL']),
)

# Application definition

INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'mathfilters',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hkg_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hkg_website.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
DEFAULT_FROM_EMAIL = os.environ['EMAIL_HOST_USER']
EMAIL_USE_TLS = True
EMAIL_PORT = 587

HKG_EMAIL = os.environ['HKG_EMAIL']

SITE_ID = 1

if DEBUG == False:
    DATABASES = {
        'default': dj_database_url.config()
    }

    STATICFILES_LOCATION = 'static'
    MEDIAFILES_LOCATION = 'media'

    STATICFILES_STORAGE = 'hkg_website.custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'hkg_website.custom_storages.MediaStorage'
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
    AWS_HEADERS = {'Cache-Control': 'max-age=86400',}
    AWS_S3_HOST = 's3.us-east-2.amazonaws.com'
    AWS_QUERYSTRING_AUTH = False

    # Production security settings
    #CSRF_COOKIE_SECURE = True
    #SESSION_COOKIE_SECURE = True
    #CONN_MAX_AGE = 3600
    #SECURE_CONTENT_TYPE_NOSNIFF = True
    #SECURE_BROWSER_XSS_FILTER = True
    #X_FRAME_OPTIONS = 'DENY'
    #SECURE_SSL_REDIRECT = True # [1]
    #SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

else:
    ALLOWED_HOSTS = [
        '127.0.0.1',
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['DATABASE_NAME'],
            'USER': os.environ['DATABASE_USER'],
            'PASSWORD': os.environ['DATABASE_PASSWORD'],
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    STATIC_URL = '/static/'

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "pages/static"),
    ]

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
    MEDIA_URL = '/media/'

    SECURE_SSL_REDIRECT = False
