from django.contrib import admin
from .models import Client, PageStatus

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created')
    list_filter = ('name', 'url')
    search_fields = ('name', 'url')

@admin.register(PageStatus)
class PageStatusAdmin(admin.ModelAdmin):
    list_display = ('body', 'status', 'client', 'created')