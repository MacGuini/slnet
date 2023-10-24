from django.shortcuts import render, redirect
from .forms import BillForm, ServiceItemForm
from .models import Bill, ServiceItem
from django.shortcuts import get_object_or_404

# Create your views here.

def createInvoice(request):
    if request.method == "POST":
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save()
            return redirect('add-service-bill', bill_id=bill.id)
    else:
        form = BillForm()

    return render(request, 'billing/create_invoice.html', {'form':form})

def addService(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    services = bill.services.all()

    if request.method == "POST":
        form = ServiceItemForm(request.POST)

        if form.is_valid():
            service_item = form.save(commit=False)
            service_item.bill = bill
            service_item.save()
            bill.total_price += service_item.price
            bill.save()

            if request.POST.get('save_and_add'):
                return redirect('add-service-bill', bill_id=bill.id)
            else:
                return redirect('invoice-details', bill_id=bill.id)
            
    else:
        form = ServiceItemForm()


    return render(request, 'billing/add_service_bill.html', {'form':form, 'bill_id':bill_id, 'bill':bill, 'services':services})
    

def invoiceDetails(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    services = bill.services.all()

    return render(request, 'billing/invoice_details.html', {'bill': bill, 'services': services})
