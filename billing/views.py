from django.shortcuts import render, redirect, get_object_or_404
from .forms import BillForm, ServiceItemForm
from .models import Bill, ServiceItem

# Create your views here.

def createInvoice(request):
    form = ServiceItemForm()

    if request.method == "POST":
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save()
            return redirect('add-service-item', bill_id=bill.id)
    else:
        form = BillForm()

    return render(request, 'billing/create_invoice.html', {'form':form})

def addServiceItem(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    services = bill.services.all()
    form = ServiceItemForm()

    if request.method == "POST":
        form = ServiceItemForm(request.POST)
        
        if form.is_valid():
            service_item = form.save(commit=False)
            service_item.bill = bill
            service_item.save()
            bill.total_price += service_item.price
            bill.save()

            if 'save_and_add' in request.POST:
                return redirect('add-service-item', bill_id=bill.id)
               
    else:
        form = ServiceItemForm()

    return render(request, 'billing/add_service_item.html', {'form':form, 'bill_id':bill_id, 'bill':bill, 'services':services})

def updateServiceItem(request, service_item_id):
    service_item = get_object_or_404(ServiceItem, id=service_item_id)
    bill = service_item.bill
    form = ServiceItemForm(instance=service_item)

    if request.method == "POST":
        old_price = service_item.price
        form = ServiceItemForm(request.POST, instance=service_item)
        
        if form.is_valid():
            service_item = form.save(commit=False)
            bill.total_price -= old_price
            bill.total_price += service_item.price
            bill.save()
            service_item.save()

            return redirect('add-service-item', bill_id=bill.id)

    return render(request, 'billing/update_service_item.html', {'form':form, 'bill':bill, 'service_item':service_item})

def deleteServiceItem(request, service_item_id):
    service_item = get_object_or_404(ServiceItem, id=service_item_id)
    bill = service_item.bill

    if request.method == "POST":
        old_price = service_item.price
        bill.total_price -= old_price
        bill.save()
        service_item.delete()
        

        return redirect('add-service-item', bill_id=bill.id)
    
    return render (request, 'delete_template.html', {'object':service_item, 'bill':bill})

def billsList(request):
    bills = Bill.objects.all()

    return render(request, "billing/bills_list.html", {'bills':bills})

    

def invoiceDetails(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    services = bill.services.all()

    return render(request, 'billing/invoice_details.html', {'bill': bill, 'services': services})
