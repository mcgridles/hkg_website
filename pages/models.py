from __future__ import unicode_literals

from django.db import models

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

    def __str__(self):
        return self.title

# Holds an image for a post
class Image(models.Model):
    post = models.ForeignKey(ExpPost, models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    img = models.ImageField()

    def __str__(self):
        return self.title

    def aspect_ratio(self):
        return float(self.img.width) / float(self.img.height)

# Journal/blog entries for a post
class Journal(models.Model):
    post = models.ForeignKey(ExpPost, models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=50)
    text = models.TextField(null=True)

    def __str__(self):
        return self.title
