from __future__ import unicode_literals

from django.contrib import admin
from .models import Author, ExpPost, Image

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

class ExpPostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['title', 'position', 'description', 'thumbnail', 'project_link', 'repo_link']}),
        ('Date information', {'fields': ['start_date', 'end_date']}),
        ('Admin information', {'fields': ['post_type', 'pub_date']}),
    ]

    inlines = [ImageInline]
    list_display = ('title', 'post_type', 'pub_date')
    search_fields = ['title']

admin.site.register(Author)
admin.site.register(ExpPost, ExpPostAdmin)
