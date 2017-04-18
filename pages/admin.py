from __future__ import unicode_literals

from django.contrib import admin
from .models import ExpPost, Author

admin.site.register(ExpPost)
admin.site.register(Author)
