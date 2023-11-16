from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

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

        bill_url = "https://sublimeimprovements.com/billing/invoice-details/" + str(bill.id)

        send_mail(
            "Hey " + bill.fname + "! You're invoice has been processed!",
            "Hello, " + bill.fname + "!\nWe have added a new bill to your account. You can view or print your invoice by visiting our site and logging into your account.\n\nIf the link below doesn't work, you can copy and paste this link into your browser to view your invoice.\n" ,
            "noreply@sublimeimprovements.com",
            [bill.email],
            fail_silently=False,
            html_message="You can view your invoice by clicking here <a href=" + bill_url + ">View invoice</a>\n\n<a href='https://sublimeimprovements.com/'>SublimeImprovements.com</a>"
        )

        print("Created Bill")

    