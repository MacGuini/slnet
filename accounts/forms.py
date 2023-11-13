from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm): # Inherets all aspects of the imported UserCreationForm
	class Meta: 
		model = User
		fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2']
		labels = {
		'first_name': 'First Name',
		'last_name': 'Last Name',
		'email': 'E-Mail',
		'username': 'Username',
		'password1': 'Password',
		'password2': 'Verify Password',
		}

	def __init__(self, *args, **kwargs):
		super(CustomUserCreationForm, self).__init__(*args, **kwargs)
		for name, field in self.fields.items():
			field.widget.attrs.update({'class': 'input'})
			field.widget.attrs.update({'class': 'form-control'})

class ProfileForm(forms.ModelForm):
	
	class Meta:
		model = Profile
		fields = '__all__'
		exclude = [
			'user',
			'username'
		]

		labels = {
			'fname':'First Name',
			'mname':'Middle Name',
			'lname':'Last Name',
			'street1':'Address',
			'street2':'Apt/Suite',
		}
		widgets = {
			'fname': forms.TextInput(attrs={ 'class': 'p-2 form-control', 'placeholder': "First Name"}),
			'mname': forms.TextInput(attrs={'class': 'p-2 form-control', 'placeholder': "Middle Name"}),
			'lname': forms.TextInput(attrs={'class': 'p-2 form-control', 'placeholder': "Last Name"}),
			'street1': forms.TextInput(attrs={'class': 'p-2 form-control', 'placeholder': "Street Address"}),
			'street2': forms.TextInput(attrs={'class': 'p-2 form-control', 'placeholder': "Apt/Suite"}),
			'city': forms.TextInput(attrs={'class': 'p-2 form-control', 'placeholder': "City"}),
			'state': forms.TextInput(attrs={'class': 'p-2 form-control', 'placeholder': "State"}),
			'zipcode': forms.TextInput(attrs={'class': 'p-2 form-control', 'placeholder': "Zipcode"}),
			'home': forms.TextInput(attrs={'class': 'p-2 form-control', 'placeholder': "Home Phone"}),
			'mobile': forms.TextInput(attrs={'class': 'p-2 form-control', 'placeholder': "Mobile Phone"}),
			'work': forms.TextInput(attrs={'class': 'p-2 form-control', 'placeholder': "Work Phone"}),
			'email': forms.TextInput(attrs={'class': 'p-2 form-control', 'placeholder': "E-Mail"}),
			'preference': forms.RadioSelect(attrs={'class': ''}),
		}
			
		# NOTE: This doesn't work for some reason
		# def __init__(self, *args, **kwargs):
		# 	super(ProfileForm, self).__init__(*args, **kwargs)

		# 	for name, field in self.fields.items():
		# 		field.widget.attrs.update({'class': 'input'})
		# 		field.widget.attrs.update({'class': 'form-control'})
		# 		field.widget.attrs.update({'class': 'p-2'})




	
