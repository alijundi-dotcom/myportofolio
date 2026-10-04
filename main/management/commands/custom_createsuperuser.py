import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Membuat superuser otomatis untuk PWS'

    def handle(self, *args, **options):
        # Bebas ganti username & password yang Anda inginkan
        username = os.environ.get('SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('SUPERUSER_EMAIL', 'admin@pws.cs.ui.ac.id')
        password = os.environ.get('SUPERUSER_PASSWORD', 'admin12345')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" berhasil dibuat!'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" sudah ada.'))