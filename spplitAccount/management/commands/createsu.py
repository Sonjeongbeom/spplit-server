import os
from django.core.management.base import BaseCommand
from spplitAccount.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(email='shc3851@likelion.org').exists():
            User.objects.create_superuser('shc3851@likelion.org', 
                                          '01012345678',
                                          'lifeisegg@00')