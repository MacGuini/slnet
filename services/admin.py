from django.contrib import admin
from .models import Service, Category, Portfolio, Comparison

# Register your models here.

admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(Comparison)
