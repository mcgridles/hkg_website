from __future__ import unicode_literals
from settings import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = [
    'henrygridley.me',
    'hkg-website.herokuapp.com',
]

DATABASES = {
    'default': dj_database_url.config()
}
