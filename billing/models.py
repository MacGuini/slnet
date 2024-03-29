from django.db import models
from decimal import Decimal
from services.models import Service
from accounts.models import Profile
from django.db.models.deletion import CASCADE, SET_NULL
import uuid

class Bill(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

    fname = models.CharField(max_length=100, null=True, blank=True)
    mname = models.CharField(max_length=100, null=True, blank=True)
    lname = models.CharField(max_length=100, null=True, blank=True)
    street1 = models.CharField(max_length=200, null=True, blank=True)
    street2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zipcode = models.CharField(max_length=5, null=True, blank=True)
    
    home = models.CharField(max_length=10, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    work = models.CharField(max_length=10, null=True, blank=True)

    email = models.EmailField(max_length=200, null=True, blank=True)

    notes = models.TextField(null=True, blank=True) 

    taxed = models.DecimalField(max_digits=9 ,decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=9 ,decimal_places=2, default=0.00)
    final_total = models.DecimalField(max_digits=9 ,decimal_places=2, default=0.00)

    isPaid = models.BooleanField(default=False)

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user is None:
            return f'User Removed - {self.total_price}'
        else:
            return f'Bill for {self.fname} {self.lname} - Total: {self.total_price}'
    def save(self, *args, **kwargs):
        tax_rate = Decimal('0.07')  # Tax rate as a decimal
        # # Ensure total_price is treated as Decimal
        # total_price_decimal = Decimal(self.total_price)
        # self.final_total = total_price_decimal + (total_price_decimal * tax_rate)
        if self.total_price > 0:
            self.taxed = self.total_price * tax_rate
            self.final_total = self.taxed + self.total_price
        super().save(*args, **kwargs)


class ServiceItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=False, blank=False)
    bill = models.ForeignKey(Bill, related_name='services', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.service is None:
            return 'Service Removed'
        else:
            return f'Service Item: {self.service.name}'