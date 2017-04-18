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

class ExpPost(models.Model):
    title = models.CharField(max_length=255)
    post_type = models.CharField(max_length=50, null=True)
    pub_date = models.DateTimeField('date published')
    #work_date = models.DateField('timespan')
    description = models.TextField()

    def __str__(self):
        return self.title
