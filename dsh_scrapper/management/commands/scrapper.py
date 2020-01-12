from django.core.management.base import BaseCommand, CommandError
import requests
from dsh_scrapper.models import Client, PageStatus


class Command(BaseCommand):
    help = 'Check site status'

    def handle(self, *args, **options):
        client_list = Client.objects.all()
        for client in client_list:
            client_url = client.url
            www_get = requests.get(client_url)
            PageStatus.objects.create(body=www_get.text, status=www_get.status_code, client=client)
            self.stdout.write(self.style.SUCCESS('Page saved  %s' % client_url))
