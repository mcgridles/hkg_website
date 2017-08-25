from __future__ import unicode_literals

from django.contrib import admin
from .models import Author, ExpPost, Image, Journal, KeyPoint

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

class KeyPointInline(admin.StackedInline):
    model = KeyPoint
    extra = 1

class JournalInline(admin.StackedInline):
    model = Journal
    extra = 1
    fields = ('title', 'author', 'text', 'pub_date')

class JournalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'author', 'text', 'post']}),
    ]
    inlines = [KeyPointInline]
    list_display = ('title', 'post')
    search_fields = ['title', 'post']

class ExpPostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['title', 'position', 'description', 'thumbnail']}),
        ('Date information', {'fields': ['start_date', 'end_date']}),
        ('Admin information', {'fields': ['post_type', 'pub_date']}),
    ]

    inlines = [ImageInline, JournalInline]
    list_display = ('title', 'post_type', 'pub_date')
    search_fields = ['title']

admin.site.register(Author)
admin.site.register(ExpPost, ExpPostAdmin)
admin.site.register(Journal, JournalAdmin)
