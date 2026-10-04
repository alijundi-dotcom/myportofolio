import sys
from django.apps import AppConfig
from django.core.management import call_command


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        # Mencegah eksekusi ganda saat membuat migrasi
        if 'runserver' in sys.argv or 'gunicorn' in sys.argv[0] or 'wsgi' in sys.argv[0]:
            try:
                call_command('custom_createsuperuser')
            except Exception as e:
                print(f"PWS Superuser Error: {e}")