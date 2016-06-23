from django.shortcuts import render
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from django.template import Context
from imd.models import Service, Category, Document
from portfolio.models import ImageGallery
from imd.forms import ContactForm

# Create your views here.
def index(request):
	form_class = ContactForm
	if request.method =='POST':
		form = form_class(request.POST, request.FILES)

		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_last_name = request.POST.get('contact_last_name', '')
			contact_email = request.POST.get('contact_email', '')
			contact_message = request.POST.get('contact_message', '')
			# contact_upload = Document(docfile=request.FILES['docfile'])
			template = get_template('contact_template.txt')
			context = Context({
					'contact_name': contact_name,
					'contact_last_name': contact_last_name,
					'contact_email': contact_email,
					'contact_message': contact_email,
					'contact_upload': contact_upload,
				})
			content = template.render(context)
			email = EmailMessage(
					"New Contact From Submission",
					content,
					['jesus@imd-sd.com'],
					headers = {'Reply-to', contact_email})
			email.send_mail()
			return redirect('services')
	documents = Document.objects.all()


	return render(request, 'index.html', {
		'services': Service.objects.all(),
		'category': Category.objects.all(),
		'gallery': ImageGallery.objects.all(),
		'form': form_class,
		})

def services(request):
	return render(request, 'services.html', {
		'services': Service.objects.all(),
		'category': Category.objects.all(),
		})

def contact(request):
	return render(request, 'contact.html', {})

def gallery(request):
	return render(request, 'gallery.html', {
		'services': Service.objects.all(),
		'category': Category.objects.all(),
		'gallery': ImageGallery.objects.all(),
		})

def vehicle_wraps(request):
	partial = ImageGallery.objects.filter(category__title='Partial Wrap')
	full = ImageGallery.objects.filter(category__title='Full Wrap')
	color = ImageGallery.objects.filter(category__title='Color Change')
	return render(request, 'vehicle_wraps.html', {
		'services': Service.objects.all(),
		'category': Category.objects.all(),
		'partial': partial,
		'full': full,
		'color': color,
		})

def tradeshows(request):
	return render(request, 'tradeshow.html', {
		'service': Service.objects.all(),
		'category':Category.objects.all(),
		})

def web_design(request):
	return render(request, 'web_design.html', {
		'service': Service.objects.all(),
		'category': Category.objects.all(),
		})

def design_service(request):
	return render(request, 'design_service.html', {
		'service': Service.objects.all(),
		'category': Category.objects.all(),
		})

def signs_banners(request):
	return render(request, 'signs_banners.html', {
		'service': Service.objects.all(),
		'category': Category.objects.all(),
		})

def printing(request):
	return render(request, 'printing.html', {
		'service': Service.objects.all(),
		'category': Category.objects.all(),
		})

def photography(request):
	return render(request, 'photography.html', {
		'service': Service.objects.all(),
		'category': Category.objects.all(),
		})

def window_wall_floor(request):
	return render(request, 'window_wall_floor.html', {
		'service': Service.objects.all(),
		'category': Category.objects.all(),
		})