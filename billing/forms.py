from django import forms
from .models import Bill, ServiceItem

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['user', 'notes', 'total_price']
        
    def __init__(self, *args, **kwargs):
        super(BillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs.update({'class': 'form-control'})

class ServiceItemForm(forms.ModelForm):
    class Meta:
        model = ServiceItem
        fields = ['service', 'description', 'bill', 'price']

    def __init__(self, *args, **kwargs):
        super(ServiceItemForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs.update({'class': 'form-control'})

