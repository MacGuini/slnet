from django import forms
from .models import Bill, ServiceItem

class BillForm(forms.ModelForm):
    
    #isPaid = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': ''}))
    class Meta:
        model = Bill
        fields = ['user', 'notes', 'isPaid']
        exclude = ['total_price', 
                   'fname', 
                   'mname',
                   'lname', 
                   'street1', 
                   'street2', 
                   'city', 
                   'state', 
                   'zipcode', 
                   'home', 
                   'work', 
                   'email']

        widgets ={
            'notes': forms.Textarea(attrs={'placeholder': "Add any details for the bill if any.", "class": "form-control"}),
            'isPaid': forms.CheckboxInput(attrs={ 'style': 'transform: scale(1.5);'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(BillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            if name != 'isPaid':
                field.widget.attrs.update({'class': 'form-control'})

class ServiceItemForm(forms.ModelForm):
    class Meta:
        model = ServiceItem
        fields = ['service', 'description','price']

    def __init__(self, *args, **kwargs):
        super(ServiceItemForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs.update({'class': 'form-control'})

