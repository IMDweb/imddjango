from __future__ import unicode_literals

from django.db import models
from imd import models as imd

# Create your models here.
class ImageGallery(models.Model):
	name = models.CharField(max_length=60)
	category = models.ForeignKey('imd.Service')
	image = models.ImageField(upload_to='galley/', blank=False, null=False)
	thumbnail = models.ImageField(upload_to='gallery/thumbnail/', blank=False, null=False)
	desc = models.TextField(max_length=250)

	def __unicode__(self):
		return "%s" % self.name

	def create_thumbnail(self):
		# if there are no image
		if not self.image:
			return

		from PIL import Image 
		from cStringIO import StringIO
		from django.core.files.uploadedfile import SimpleUploadedFile
		import os

		# max Thumbnail side
		THUMBNAIL_SIZE = (250, 250)

		DJANGO_TYPE = self.image.file.content_type

		if DJANGO_TYPE == 'image/jpeg':
			PIL_TYPE = 'jpeg'
			FILE_EXTENTION = 'jpg'
		elif DJANGO_TYPE == 'image/png':
			PIL_TYPE = 'png'
			FILE_EXTENTION = 'png'

		#open original photo 
		image = Image.open(StringIO(self.image.read()))

		image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

		# save thumbnail
		temp_handle = StringIO()
		image.save(temp_handle, PIL_TYPE)
		temp_handle.seek(0)

		# save image to a SimpleUplodedFile to save into ImageField
		suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
			temp_handle.read(), content_type=DJANGO_TYPE)
		# save SimpleUploadedFile into imagefield
		self.thumbnail.save('%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENTION), suf, save=False)

	

	def save(self):
		#create thumbnail
		self.create_thumbnail()
		#self.resizeImage()
		super(ImageGallery, self).save()