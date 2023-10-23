from django.urls import path
from . import views

urlpatterns = [
    path('billing/create-invoice/', views.createInvoice, name='create-invoice')
]
