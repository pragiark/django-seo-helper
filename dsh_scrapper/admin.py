from django.contrib import admin
from dsh_scrapper.models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
