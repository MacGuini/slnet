from django.forms import ModelForm
from django import forms
from .models import Service, Category

class ServiceForm(forms.ModelForm):
    

    class Meta:
        model = Service
        fields = ("__all__")

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name the service'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe what the service provides'}),
            # image doesn't render Clear checkbox on templates
            'image': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)

       
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs.update({'class': 'form-control'})

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ("__all__")


    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

       
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs.update({'class': 'form-control'})  

