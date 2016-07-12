from django import forms

class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True, max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}))
	contact_last_name = forms.CharField(required=True, max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))
	contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	contact_subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	contact_message = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['contact_name'].label = "First Name:"
		self.fields['contact_last_name'].label = "Last Name:"
		self.fields['contact_email'].label = "Email:"
		self.fields['contact_subject'].label = "Subject:"
		self.fields['contact_message'].label = "Message:"
