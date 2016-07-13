from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from imd.models import Service, Category, Document
from portfolio.models import ImageGallery
from imd.forms import ContactForm

# Create your views here.

@xframe_options_exempt
def index(request):
	return render(request, 'index.html', {
		'services': Service.objects.all(),
		'category': Category.objects.all(),
		'gallery': ImageGallery.objects.all(),
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

def contact(request):
	if request.method == 'GET':
		form = ContactForm
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['contact_subject']
			email = form.cleaned_data['contact_email']
			first_name = form.cleaned_data['contact_name']
			last_name = form.cleaned_data['contact_last_name']
			message = form.cleaned_data['contact_message']
			template = get_template('contact_template.txt')
			context = Context({
				'contact_first_name': first_name,
				'contact_last_name': last_name,
				'contact_email': email,
				'contact_subject': subject,
				'message': message,
			})
			content = template.render(context)
			email_message = EmailMessage(
				"New Contact Message",
				content,
				email,
				['jesus@imd-sd.com']
			)
			try:
				email_message.send()
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
		return redirect('thanks')
	return render(request, 'contact.html', {
			'form': form,
		})
def thanks(request):
	return render(request, 'thank_you.html')