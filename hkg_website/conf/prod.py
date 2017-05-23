from __future__ import unicode_literals
from base import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = [
    'henrygridley.me',
    'hkg-website.herokuapp.com',
]

DATABASES = {
    'default': dj_database_url.config()
}
