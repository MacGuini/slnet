from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import uuid

from django.db.models.deletion import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f'{self.name} category'

    class Meta:
        ordering = ['name']


class Service(models.Model):
    class Priority(models.IntegerChoices):
        FIRST = 1
        SECOND = 2
        THIRD = 3
        FORTH = 4
        FIFTH = 5

    SERVICE_TYPE = (
        ('featured', 'Featured'),
        ('other', 'Other'),
        ('none', 'None'),
        )

    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=300, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=False, blank=False)
    featured = models.CharField(max_length=9, null=False, blank=False, choices=SERVICE_TYPE, default='none')
    priority = models.IntegerField(choices=Priority.choices, blank=True, null=True)

    categories = models.ManyToManyField(Category, blank=True)

 
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f'{self.name} service'
    
    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Service, self).save(*args, **kwargs)

    class Meta:
        ordering = ['priority', '-created']




class Portfolio(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default='unamed')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

class Comparison(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    before = models.ImageField(null=False, blank=False)
    after = models.ImageField(null=False, blank=False)

    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ['-created']
    