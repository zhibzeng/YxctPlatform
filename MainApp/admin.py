from django.contrib import admin
from .models import Person

# Register your models here.
class Person(admin.ModelAdmin):
    """docstring for NotificationAdmin"""
    list_display = ('first_name', 'last_name')
    list_filter = ('first_name',)
    ordering = ('-first_name',)