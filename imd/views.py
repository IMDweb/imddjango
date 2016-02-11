from django.shortcuts import render
from imd.models import Service, Category, Gallery

# Create your views here.
def index(request):
	return render(request, 'index.html')

def services(request):
	return render(request, 'services.html', {
		'services': Service.objects.all(),
		'category': Category.objects.all(),
		})

def gallery(request, title):
	return render('gallery.html', {
		'gallery': Gallery.objects.all()
		})
