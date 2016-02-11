from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink

# Create your models here.
def upload_images_to(filename):
	return os.path.join('media/images/{0}'.format(filename))

class Service(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	category = models.ForeignKey('imd.Category')
	description = models.TextField()
	image = models.ImageField(upload_to=)

	def __unicode__(self):
		return "%s service" % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_service', None, { 'title': self.slug })

class Category(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)

	def __unicode__(self):
		return "%s" % self.name

	@permalink
	def get_absolute_url(self):
		return ('view_service_category', None, { 'slug': self.slug })

class Gallery(models.Model):
	title = models.CharField(max_length=100, unique=True)
	image = models.ImageField()
	category = models.ForeignKey('imd.Category')
	published = models.DateTimeField(db_index=True, auto_now_add=True)
	description = models.TextField()

	def __unicode__(self):
		return "%s" % self.title