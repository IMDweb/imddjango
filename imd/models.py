from __future__ import unicode_literals

import os
from django.db import models
from django.db.models import permalink

# Create your models here.
def upload_images_to(instance, filename):
	return os.path.join("images/services/", filename)

class Service(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	category = models.ForeignKey('imd.Category')
	description = models.TextField()
	image = models.ImageField(upload_to=upload_images_to, blank=True)

	def __unicode__(self):
		return "%s service" % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_service', None, { 'title': self.slug })

class Category(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	desc = models.TextField()

	def __unicode__(self):
		return "%s" % self.name

	@permalink
	def get_absolute_url(self):
		return ('view_service_category', None, { 'slug': self.slug })

class Document(models.Model):
	docfile = models.FileField(upload_to='documents/%y/%m/', blank=True, null=True)