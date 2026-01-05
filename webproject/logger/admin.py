from django.contrib import admin

# Register your models here.
# admin.py
#from django.contrib import admin
from .models import RequestLog

@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ['view_name', 'method', 'duration', 'timestamp']
    list_filter = ['view_name', 'method', 'timestamp']