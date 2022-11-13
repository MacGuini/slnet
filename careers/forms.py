from django.forms import ModelForm
from django import forms
from .models import Application, Job
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

import datetime

# Allows start field to have the date input type in their HTML template types
class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicationForm(forms.ModelForm):

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    
    class Meta:
        
        model = Application
        fields = ("fname","lname","dob", "street1", "street2", "city", "state", "zipcode", "mobile", "home", "work", "email", "preference", "resume", "start",  "experience", "bio","skills", "schedule", "job")

        


        widgets = {

            'fname': forms.TextInput(attrs={'placeholder': 'John'}),
            'lname': forms.TextInput(attrs={'placeholder': 'Doe'}),
            'street1': forms.TextInput(attrs={'placeholder': '123 Main St'}),
            'street2': forms.TextInput(attrs={'placeholder': 'Apt #'}),
            'city': forms.TextInput(attrs={'placeholder': 'Trenton'}),
            'state': forms.TextInput(attrs={'placeholder': 'NJ'}),
            'zipcode': forms.TextInput(attrs={'placeholder': '12345'}),
            'mobile': forms.TextInput(attrs={'placeholder': '5551235555'}),
            'home': forms.TextInput(attrs={'placeholder': '5551235555'}),
            'work': forms.TextInput(attrs={'placeholder': '5551235555'}),
            'email': forms.TextInput(attrs={'placeholder': 'example@email.com'}),
            'bio': forms.Textarea(attrs={'placeholder': "Tell us more about yourself. How would you make a sublime addition to our team?", 'label': 'Bio' }),
            'skills': forms.Textarea(attrs={'placeholder': "What skills do you posses?" }),
            'schedule': forms.Textarea(attrs={'placeholder': "Anything we need to know about your schedule?" }),


            # Creates Date input field drop menu
            'start' : DateInput(),
            'dob' : DateInput(),


        }

    # 2.5MB - 2621440
    # 5MB - 5242880
    # 10MB - 10485760
    # 20MB - 20971520
    # 50MB - 5242880
    # 100MB 104857600
    # 250MB - 214958080
    # 500MB - 429916160
    MAX_UPLOAD_SIZE = 10485760

    # ERROR AND VALIDATION MANAGEMENT #


    def clean_mobile(self, *args, **kwargs):
        mobile = self.cleaned_data.get("mobile")

        if mobile:
            if mobile.isdigit()==False:
                raise forms.ValidationError("Only Numbers")
        return mobile

    def clean_home(self, *args, **kwargs):
        home = self.cleaned_data.get("home")
        if home:
            if home.isdigit()==False:
                raise forms.ValidationError("Only Numbers")
        return home

    def clean_work(self, *args, **kwargs):
        work = self.cleaned_data.get("work")
        if work:
            if work.isdigit()==False:
                raise forms.ValidationError("Only Numbers")
        return work
    
    def clean_dob(self, *args, **kwargs):
        dob = self.cleaned_data.get("dob")
        age = (datetime.date.today() - dob).days/365
        if age <18:
            raise forms.ValidationError('Must be 18 years or older to apply.')
        return dob
    
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

        # for loop iterates all fields
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            # Remove below if using the exception script below
            field.widget.attrs.update({'class': 'form-control'})


class ReviewAppForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ("status",)


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('title', 'description', 'pay', 'rate',)

        widgets = {
            'title' : forms.TextInput(attrs={'placeholder': 'Job Title'}),
            'description' : forms.Textarea(attrs={'placeholder': 'Job Description'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)

        # for loop iterates all fields
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            # Remove below if using the exception script below
            field.widget.attrs.update({'class': 'form-control'})
