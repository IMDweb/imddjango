from django import forms

def upload_to(instance, ):
	pass

class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True, max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}))
	contact_last_name = forms.CharField(required=True, max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))
	contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	contact_message = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
	contact_upload = forms.FileField(help_text='max. 42 megabytes')

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['contact_name'].label = "First Name:"
		self.fields['contact_last_name'].label = "Last Name:"
		self.fields['contact_email'].label = "Email:"
		self.fields['contact_message'].label = "Message:"
		self.fields['contact_upload'].label = "Upload File:"
