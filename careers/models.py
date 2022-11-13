from django.db import models
import uuid
from .validators import validate_file_size
from django.core.validators import FileExtensionValidator

# Create your models here.
class Job(models.Model):
    RATE_TYPE = (
        ('hour', 'Per Hour'),
        ('salary', 'Salary'),
        ('flat', 'Flat'),
        ('interview', 'Discussed at Interview'),
        ('none', 'None posted'),
    )
    title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(null=False, blank=False)
    pay = models.DecimalField(max_digits=20, null=True, blank=True, decimal_places=2)
    rate = models.CharField(max_length=20, choices=RATE_TYPE)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS_TYPE = (
        ('accept', 'Accept'),
        ('reject', 'Reject'),
        ('pending', 'Pending'),
    )

    CONTACT_TYPE = (
        ('mobile', 'Call Mobile'),
        ('home', 'Call Home'),
        ('work', 'Call Work'),
        ('text', 'Text Mobile'),
        ('email', 'Email'),
    )
    fname = models.CharField(max_length=100, null=False, blank=False)
    lname = models.CharField(max_length=100, null=False, blank=False)
    street1 = models.CharField(max_length=200, null=False, blank=False)
    street2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=2, null=False, blank=False)
    zipcode = models.CharField(max_length=5, null=False, blank=False)

    dob = models.DateField(null=False, blank=False)

    mobile = models.CharField(max_length=10, null=True, blank=True)

    home = models.CharField(max_length=10, null=True, blank=True)

    work = models.CharField(max_length=10, null=True, blank=True)

    email = models.EmailField(max_length=200, null=True, blank=True)
    preference = models.CharField(max_length=11, choices=CONTACT_TYPE, default='mobile', null=False, blank=False)

    job = models.ForeignKey(Job, on_delete=models.CASCADE, blank=True, null=True)
    resume = models.FileField(null=True, blank=True, upload_to='resumes/', validators=[validate_file_size, FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf'])])
    start = models.DateField(null=False, blank=False)
    experience = models.PositiveSmallIntegerField(blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    schedule = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=7, choices=STATUS_TYPE, default='pending', null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)



    def __str__(self):
        return self.lname + ", " + self.fname

    class Meta:
        ordering = ["-created"]
