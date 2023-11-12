from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Bill

@receiver(post_save, sender=Bill)
def createBill(sender, instance, created, **kwargs):
    if created:
        bill = instance

        bill.fname = bill.user.fname
        bill.lname = bill.user.lname
        bill.street1 = bill.user.street1
        bill.street2 = bill.user.street2
        bill.city = bill.user.city
        bill.state = bill.user.state
        bill.zipcode = bill.user.zipcode
        bill.home = bill.user.home
        bill.mobile = bill.user.mobile
        bill.work = bill.user.work
        bill.email = bill.user.email
        
        bill.save()

        print("Created Bill")