from django.urls import path
from . import views

urlpatterns = [
    path('billing/create-invoice/', views.createInvoice, name='create-invoice'),
    path('billing/add-service-item/<uuid:bill_id>/', views.addServiceItem, name='add-service-item'),
    path('billing/invoice-details/<uuid:bill_id>/', views.invoiceDetails, name='invoice-details'),
    path('billing/update-service-item/<uuid:service_item_id>/', views.updateServiceItem, name="update-service-item"),
    path('billing/delete-service-item/<uuid:service_item_id>/', views.deleteServiceItem, name="delete-service-item"),
    path('billing/bills-list/', views.billsList, name='bills-list'),
    path('billing/update-invoice/<uuid:bill_id>/', views.updateInvoice, name='update-invoice'),
    path('billing/itemized-table/<uuid:bill_id>/', views.itemizedTable, name='itemized-table'),
]
