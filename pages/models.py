from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.sitemaps import ping_google

# Holds information for the AboutMe page
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()
    email = models.EmailField()
    picture = models.ImageField(null=True)

    def __str__(self):
        return self.name

# General post class - can be used for projects, work, volunteering, etc.
class ExpPost(models.Model):
    title = models.CharField(max_length=255)
    position = models.CharField(max_length=255, null=True, blank=True)
    post_type = models.CharField(max_length=50, null=True)
    pub_date = models.DateTimeField('date published')
    start_date = models.DateField('date work started', null=True)
    end_date = models.DateField('date work ended', null=True, blank=True)
    description = models.TextField()
    marquee = models.ImageField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pages:details', kwargs={'pk':self.id})

    def save(self, force_insert=False, force_update=False):
        super(ExpPost, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass

# Holds an image for a post
class Image(models.Model):
    post = models.ForeignKey(ExpPost, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    img = models.ImageField()

    def __str__(self):
        return self.title

# Journal/blog entries for a post
class Journal(models.Model):
    post = models.ForeignKey(ExpPost, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=50)
    text = models.TextField(null=True)

    def __str__(self):
        return self.title

class KeyPoint(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.text
