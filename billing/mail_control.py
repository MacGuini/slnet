from django.core.mail import send_mail
from .models import Bill

def updateMail(name, email, bill_url):

    send_mail(
        "Hey " + name + "! You're invoice has been processed!",
        "Hello, " + name + "!\nWe have updated a bill on your account.\nYou can view or print your invoice by visiting our site and logging into your account.\n\nIf the link below doesn't work, you can copy and paste this link into your browser to view your invoice.\n" ,
        "noreply@sublimeimprovements.com",
        [email],
        fail_silently=False,
        html_message="You can view your invoice by clicking here <a href=" + bill_url + ">View invoice</a>\n\nIf you believe this email was sent in error or you have any questions, please visit us at <a href='https://sublimeimprovements.com/'>SublimeImprovements.com</a>. Scroll to the bottom of any page for our contact information."
    )

def createBillUrl(bill_id):
    bill_url = "https://sublimeimprovements.com/billing/invoice-details/" + str(bill_id)
    return bill_url