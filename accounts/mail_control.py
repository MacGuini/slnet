from django.core.mail import send_mail


def newAccount(name, username, email, password):
    send_mail(
        "Hello, " + name + "! We've created an account for you at Sublime Improvements",
        "We've created a new account just for you at Sublime Improvements. You are recieving this message as a confirmation. You do not need to access your account to use our services. But if you would like to view any invoices we've issued to you. You can log in at sublimeimprovements.com/login/ using these credentials.\n\nUsername: " + username + "\nRandomly Generated Password: " + password + "\n\nWe recommend that you change your password after logging on. You can do this by clicking 'Edit Account' in the nav bar after you've signed in.\nIf your password doesn't work or you can't remember it, click the 'Forgot Password' button at the bottom of the login page. Enter your email into the input box and you'll receive instructions on how to create a new password.\nThank you for choosing Sublime Improvements!",
        "noreply@sublimeimprovements.com",
        [email],
        fail_silently=False,
    )
def updateAccounts(name, email):
	send_mail(
		"Hey " + name+ "! Your profile was updated!", # Subject
		"This message is being sent to you to let you know that your profile at sublimeimprovements.com has been successfully updated.", # Message
		"noreply@sublimeimprovements.com", # From
		[email], # To
		fail_silently=False,
		)
