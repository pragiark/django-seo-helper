from django.core.management.base import BaseCommand

from dsh_scrapper.models import Client


class Command(BaseCommand):
    help = 'Add record do database using django-admin commands'

    def add_arguments(self, parser):
        parser.add_argument('name')
        parser.add_argument('url')

    def handle(self, *args, **options):
        name = options['name']
        url = options['url']
        success = Client.objects.create(name=name, url=url)
        self.stdout.write(self.style.SUCCESS('Successfully add %s' % success))
