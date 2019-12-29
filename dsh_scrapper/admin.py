from django.contrib import admin
from dsh_scrapper.models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created')
    list_filter = ('name', 'url')
    search_fields = ('name', 'url')
