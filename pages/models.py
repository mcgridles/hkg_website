from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    major = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    picture = models.ImageField(null=True)

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField()

    def __str__(self):
        return self.title

#class Journal(models.Model):

class ExpPost(models.Model):
    title = models.CharField(max_length=255)
    position = models.CharField(max_length=255, null=True, blank=True)
    post_type = models.CharField(max_length=50, null=True)
    pub_date = models.DateTimeField('date published')
    start_date = models.DateField('date work started', null=True)
    end_date = models.DateField('date work ended', null=True, blank=True)
    description = models.TextField()
    images = models.ManyToManyField(ImageModel, blank=True)

    def __str__(self):
        return self.title
