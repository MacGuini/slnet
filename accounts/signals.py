from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from django.contrib.auth.models import User
from .models import Profile
from billing.models import Bill
from django.core.mail import send_mail
import string, secrets, random

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

# Generate a 10-character random password
password = generate_password(10)
print("\n\nPASSWORD:" + password + "\n\n")

@receiver(post_save, sender=Profile)
def createClient(sender, instance, created, **kwargs):
	if created:
		profile = instance 

		fname = str(profile.fname)
		lname = str(profile.lname)
		username = str(profile.username)
		email = str(profile.email)
		password = generate_password(random.randint(15, 25))

		user = User.objects.create_user(username, email, password)

		user.first_name = fname
		user.last_name = lname
		user.save()

		profile.user = user
		profile.save()

		send_mail(
			"Successfully created a Sublime Improvements account for " + fname + " " + lname,
			"This message is to inform you that a new account was successfully created on Sublime Improvements.\n\n\nUsername: "+ username + "\n\nName: " + fname + " " + lname,
			'noreply@sublimeimprovements.com',
			['bhatz829@gmail.com', email],
			fail_silently=False
			)


# @receiver(post_save, sender=User)
# def createProfile(sender, instance, created, **kwargs):
# 	if created:
# 		user = instance
# 		profile = Profile.objects.create(
# 			user = user,
# 			username = user.username,
# 			email = user.email,
# 			fname = user.first_name,
# 			lname = user.last_name,
# 		)
# 		profile.save()

# 		send_mail(
# 			"An account has been created on Sublime Improvements",
# 			"This message is to inform you that a new account has been created on Sublime Improvements.\n\nUsername: "+ user.username + "\n\nIf this user was not authorized please contact your administrator, Brian Lindsay."
# 			'noreply@sublimeimprovements.com',
# 			['bhatz829@gmail.com'],
# 			fail_silently=False
# 		)
		
# 		if profile.email:
# 			send_mail(
# 			"Hey " + profile.fname + " " + profile.lname + "! Your profile was created!", # Subject
# 			"This message is being sent to you to let you know that your profile at sublimeimprovements.com has been successfully created.", # Message
# 			"noreply@sublimeimprovements.com", # From
# 			[profile.email], # To
# 			fail_silently=False,
# 		)

		
@receiver(post_save, sender=Profile)
def updateProfile(sender, instance, created, **kwargs):
	profile = instance
	user = profile.user
	bills = Bill.objects.filter(user=profile)

	if created == False:
		user.first_name = profile.fname 
		user.last_name = profile.lname
		user.email = profile.email
		user.save()

		if bills:
			for bill in bills:
				bill.fname = profile.fname 
				bill.lname = profile.lname
				bill.street1 = profile.street1
				bill.street2 = profile.street2
				bill.city = profile.city
				bill.state = profile.state
				bill.zipcode = profile.zipcode
				bill.home = profile.home
				bill.mobile = profile.mobile
				bill.work = profile.work
				bill.email = profile.email
				bill.save()

		send_mail(
			"Hey " + profile.fname + " " + profile.lname + "! Your profile was updated!", # Subject
			"This message is being sent to you to let you know that your profile at sublimeimprovements.com has been successfully updated.", # Message
			"noreply@sublimeimprovements.com", # From
			[profile.email], # To
			fail_silently=False,
		)

@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
	try:
		user = instance.user
		user.delete()
	except:
		pass