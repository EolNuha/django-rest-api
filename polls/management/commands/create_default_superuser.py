from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings

class Command(BaseCommand):
    help = 'Create a default superuser if one does not already exist'

    def handle(self, *args, **kwargs):
        username = getattr(settings, 'DJANGO_SUPERUSER_USERNAME', 'admin')
        email = getattr(settings, 'DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = getattr(settings, 'DJANGO_SUPERUSER_PASSWORD', 'admin')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
