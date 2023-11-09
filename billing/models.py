from django.db import models
from services.models import Service
from accounts.models import Profile
from django.db.models.deletion import CASCADE
import uuid

class Bill(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=9 ,decimal_places=2, default=0.00)
    isPaid = models.BooleanField(default=False)

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.fname} {self.user.lname} - {self.total_price}'

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
            return f'{self.service.name}'