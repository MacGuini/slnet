from django.contrib import admin
from .models import Bill, ServiceItem

# Register your models here.

admin.site.register(Bill)
admin.site.register(ServiceItem)