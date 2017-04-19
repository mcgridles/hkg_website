from __future__ import unicode_literals

from django.contrib import admin
from .models import Author, ExpPost, Image, Journal

admin.site.register(Author)
admin.site.register(ExpPost)
admin.site.register(Image)
admin.site.register(Journal)
