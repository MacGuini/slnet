from django.urls import path
from . import views

urlpatterns = [
    path('billing/create-invoice/', views.createInvoice, name='create-invoice'),
    path('billing/add-service-bill/<uuid:bill_id>/', views.addService, name='add-service-bill'),
    path('billing/invoice-details/<uuid:bill_id>/', views.invoiceDetails, name='invoice-details'),

]
