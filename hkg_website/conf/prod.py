from __future__ import unicode_literals
from base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = [
    'henrygridley.me',
    'hkg-website.herokuapp.com',
]

DATABASES = {
    'default': dj_database_url.config()
}

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#AWS_S3_SECURE_URLS = False  # use http instead of https
#AWS_QUERYSTRING_AUTH = False    # don't add complex authentication-related query parameters for requests
#AWS_AUTO_CREATE_BUCKET = False
#AWS_EXPIRY = 60 * 60 * 24 * 7
#AWS_S3_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']  # Your S3 Access Key
#AWS_S3_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']  # Your S3 Secret
#AWS_STORAGE_BUCKET_NAME = 'hkg-website-assets'
#AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'  # Change to the media center you chose when creating the bucket
#AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#AWS_HEADERS = {
#    'Cache-Control': six.b('max-age=%d, s-maxage=%d, must-revalidate' % (
#        AWS_EXPIRY, AWS_EXPIRY))
#}

# the next monkey patch is necessary to allow dots in the bucket names
#import ssl
#if hasattr(ssl, '_create_unverified_context'):
#   ssl._create_default_https_context = ssl._create_unverified_context

#MEDIA_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
#STATICFILES_STORAGE = DEFAULT_FILE_STORAGE
#STATIC_URL = MEDIA_URL
