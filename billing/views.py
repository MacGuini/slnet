from django.shortcuts import render, redirect
from .forms import BillForm, ServiceItemForm

# Create your views here.

def createInvoice(request):
    if request.method == "POST":
        bill_form = BillForm(request.POST)
        service_item_form = ServiceItemForm(request.POST)
        if bill_form.is_valid() and service_item_form.is_valid():
            bill = bill_form.save()
            service_item = service_item_form.save(commit=False)
            service_item.bill = bill
            service_item.save()
            return redirect('invoice_detail', pk=bill.pk)
    else:
        bill_form = BillForm()
        service_item_form = ServiceItemForm()
    return render(request, 'billing/create_invoice.html', {'bill_form': bill_form, 'service_item_form': service_item_form})
