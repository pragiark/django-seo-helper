from django.core.management.base import BaseCommand, CommandError
from dsh_scrapper.models import Client


class Command(BaseCommand):
    help = 'Add record do database using django-admin commands'

    def add_arguments(self, parser):
        parser.add_argument('name')
        parser.add_argument('url')

    def handle(self, *args, **options):
        name_var = options['name']
        url_var = options['url']
        sucess_var = Client.objects.create(name=name_var, url=url_var)
        self.stdout.write(self.style.SUCCESS('Successfully add %s' % sucess_var))
