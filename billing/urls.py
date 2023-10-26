from django.urls import path
from . import views

urlpatterns = [
    path('billing/create-invoice/', views.createInvoice, name='create-invoice'),
    path('billing/add-service-item/<uuid:bill_id>/', views.addServiceItem, name='add-service-item'),
    path('billing/invoice-details/<uuid:bill_id>/', views.invoiceDetails, name='invoice-details'),

]
