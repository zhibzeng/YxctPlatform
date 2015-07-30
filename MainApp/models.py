from django.db import models
from django.contrib import admin
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __unicode__(self):
        return u'%s' % (self.name)
